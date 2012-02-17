# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()


urlpatterns = patterns(
    '',
    # url(r'^something/',
    #     direct.import.views.some_method,
    #     name="name_it"),
    # Only needed when developing on lizard_fiber.
    url(r'^admin/', include(admin.site.urls)),
    # Fiber urls. This means lizard_fiber's urls needs to be mounted as ''.
    (r'^api/v1/', include('fiber.api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
    # Fiber catch-all. Needs to be at the end.
    (r'', 'fiber.views.page'),
    )
urlpatterns += debugmode_urlpatterns()
