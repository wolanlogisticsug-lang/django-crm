from WOLANCRM.conf import settings
from WOLANCRM.views.generic.base import RedirectView


class FaviconRedirect(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        url = '/static/favicon.ico'
        if settings.DEBUG:
            url = '/static/common/favicon_dev.ico'

        return url

