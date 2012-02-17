import logging

from django.conf import settings
from lizard_ui.configchecker import register

logger = logging.getLogger(__name__)


@register
def checker():
    """Verify lizard_fiber's demands on settings.py."""
    if not hasattr(settings, 'FIBER_DEFAULT_TEMPLATE'):
        logger.error(
            "You haven't set a default template for fiber. Suggestion:\n"
            "FIBER_DEFAULT_TEMPLATE = 'lizard_fiber/base.html'")
    for app in ['piston',
                'mptt',
                'fiber',
                ]:
        if app not in settings.INSTALLED_APPS:
            logger.error("%s is missing from INSTALLED_APPS.", app)
    if not ('fiber.middleware.AdminPageMiddleware'
            in settings.MIDDLEWARE_CLASSES):
        logger.error("fiber.middleware.AdminPageMiddleware is missing from "
                     "MIDDLEWARE_CLASSES")
    for processor in ['django.core.context_processors.request',
                      'fiber.context_processors.page_info']:
        if not processor in settings.TEMPLATE_CONTEXT_PROCESSORS:
            logger.error("%s is missing from TEMPLATE_CONTEXT_PROCESSORS",
                         processor)

