import requests
from .errors import ApiError


class Products:
    ENDPOINT = "/api/products/"

    def __init__(self, url):
        self._url = url

    def items(self, category=None):
        """
        Generator interface to fetch products one-by-one
        Optional category filter may be used to return only products
        that match it.
        """
        for page in self.pages():
            for obj in page["objects"]:
                if not category:
                    yield obj
                elif category == obj["category"]:
                    yield obj

    def pages(self, start_index="1"):
        """
        Generator interface to fetch products page-by-page
        """
        next_page_ref = self.ENDPOINT + start_index
        while next_page_ref:
            page = self._get_page(next_page_ref)
            yield page
            next_page_ref = page.get("next", None)

    def _get_page(self, page_ref):
        page_url = self._url + page_ref

        try:
            response = requests.get(page_url)
            if response.status_code != requests.codes.ok:
                response.raise_for_status()

        except requests.exceptions.ConnectionError:
            raise ApiError("Failed to connect to the server")
        except requests.exceptions.Timeout:
            raise ApiError("Failed to connect to the server: timeout")
        except requests.exceptions.HTTPError:
            raise ApiError("Server returned error")

        return response.json()
