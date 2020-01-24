CONVERSION_FACTOR = 250


def calculate_cubic_weight(width, length, height):
    """
    Calculates cubic weigh for the specified volume

    :param width: dimension in meters
    :param length: dimension in meters
    :param height: dimension in meters
    :return: calculated cubic weigh in kilogrammes
    """
    volume = width * length * height
    return volume * CONVERSION_FACTOR


def calculate_average_cubic_weight(items):
    """
    Calculates average cubic weigh for all the items.

    Each item is a dictionary that shall has the
    following mandatory fields:
        {
            "size": {
                "width": 49.6,
                "length": 38.7,
                "height": 89.0
            }
        }

    Each dimension is in centimeters

    :param items: iterable object
    :return: calculated average cubic weigh in kilogrammes
    """
    count = 0
    cubic_weight = 0

    for item in items:
        size = item['size']
        cubic_weight += calculate_cubic_weight(
            size['width'] / 100,
            size['length'] / 100,
            size['height'] / 100
        )
        count += 1

    if not count:
        return 0
    else:
        return cubic_weight / count
