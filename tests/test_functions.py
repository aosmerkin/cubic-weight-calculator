from calculator.functions import \
    calculate_cubic_weight, calculate_average_cubic_weight


def test_calculate_cubic_weight():
    """
    Check that we calculate cubic weight correctly.
    All dimensions are expected to be in meters
    """
    assert calculate_cubic_weight(2, 3, 5) == 7500


def test_calculate_average_cubic_weight_with_empty_list():
    """
    Check that we do not mess if items list is empty
    """
    assert calculate_average_cubic_weight([]) == 0


def test_calculate_average_cubic_weight():
    """
    Check that we can calculate average cubic weight
    for the items in provided list.
    All dimensions are expected to be in centimeters.
    """
    items = [
        {
            "size": {
                "width": 20,
                "length": 30,
                "height": 50
            }
        },
        {
            "size": {
                "width": 10,
                "length": 20,
                "height": 10
            }
        },
    ]

    assert calculate_average_cubic_weight(items) == 4


