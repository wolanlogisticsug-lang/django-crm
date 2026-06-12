from WOLANCRM.contrib.sites.models import Site
from WOLANCRM.test import RequestFactory
from WOLANCRM.test import TestCase
from WOLANCRM.urls import reverse

from common.utils.secure_url import secure_url


class TestSecureUrl(TestCase):

    def test_secure_url(self):
        print(" Run Test Method:", self._testMethodName)
        
        relative_url = reverse("site:crm_company_changelist")
        factory = RequestFactory()
        # Create an instance of a GET request.
        request = factory.get(relative_url)
        self.assertEqual(relative_url, secure_url(relative_url, request))
        site = Site.objects.get_current()
        https_url = f"https://{site.domain}{relative_url}"
        self.assertEqual(https_url, secure_url( https_url, factory.get(https_url)))

        http_url = f"http://{site.domain}{relative_url}"
        self.assertEqual(http_url, secure_url( http_url, factory.get(https_url)))
                
        # alien domain
        url = f"https://www.google.com{relative_url}"

        self.assertEqual('/', secure_url(url, factory.get(url)))
