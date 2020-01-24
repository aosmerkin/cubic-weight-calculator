from unittest.mock import Mock, patch, call
from calculator.api import Products


@patch("requests.get")
def test_products_produces_pages(mocked_get):
    """
    Tests that we can access first page and use correct url
    """
    mocked_get.side_effect = [
        Mock(
            status_code=200,
            json=Mock(
                return_value={'objects': []}
            )
        )
    ]

    products = Products(
        "http://some_url"
    )

    for page in products.pages():
        assert page['objects'] == []

    mocked_get.assert_called_once_with(
        'http://some_url/api/products/1'
    )


@patch("requests.get")
def test_products_pages_follow_next_link(mocked_get):
    """
    Test that we can iterate over pages by following 'next' link
    """
    mocked_get.side_effect = [
        Mock(
            # First page with the link to the next page
            status_code=200,
            json=Mock(
                return_value={
                    'objects': [],
                    'next': "/api/products/X"
                }
            )
        ),
        Mock(
            # Last page: no next link
            status_code=200,
            json=Mock(
                return_value={
                    'objects': [],
                }
            )
        )

    ]

    products = Products(
        "http://some_url"
    )

    pages = []
    for page in products.pages():
        pages.append(page)

    assert len(pages) == 2

    mocked_get.assert_has_calls(
        [call('http://some_url/api/products/1')],
        [call('http://some_url/api/products/X')]
    )


@patch("requests.get")
def test_products_produces_items(mocked_get):
    """
    Tests that we can access items one-by-one
    """
    mocked_get.side_effect = [
        Mock(
            status_code=200,
            json=Mock(
                return_value={
                    'objects': [
                        {'item': 'Item One'},
                        {'item': 'Item Two'},
                        {'item': 'Item Three'}
                    ]
                }
            )
        )
    ]

    products = Products(
        "http://some_url"
    )

    items = []
    for item in products.items():
        items.append(item)

    assert len(items) == 3
    assert items[2]['item'] == 'Item Three'


@patch("requests.get")
def test_products_items_can_be_filtered(mocked_get):
    """
    Tests that we can access only items of given category
    """
    mocked_get.side_effect = [
        Mock(
            status_code=200,
            json=Mock(
                return_value={
                    'objects': [
                        {'category': 'Category One'},
                        {'category': 'Category Two'},
                        {'category': 'Category Three'}
                    ]
                }
            )
        )
    ]

    products = Products(
        "http://some_url"
    )

    items = []
    for item in products.items('Category Two'):
        items.append(item)

    assert len(items) == 1
    assert items[0]['category'] == 'Category Two'
