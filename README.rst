lizard-fiber
==========================================

Lizard-fiber is a small wrapper around `django-fiber
<https://github.com/ridethepony/django-fiber>`_ to integrate it into lizard
sites.

- A configchecker (``bin/django check_config``) tells you if you have to
  adjust your settings.

- At the **end** of your urls, you need to mount lizard_fiber's urls. And it
  needs to be mounted on the root (so on an empty string). This is required by
  django-fiber.  So it should look like this::

    urlpatterns = patterns(
        '',
        url(ALL_YOUR_REGULAR_STUFF),
        ...
        # lizard_fiber catch-all. Needs to be at the end.
        url(r'', include('lizard_fiber.urls')),
        )


