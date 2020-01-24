CONVERSION_FACTOR = 250


def calculate_cubic_weight(width, length, height):
    volume = width * length * height
    return volume * CONVERSION_FACTOR


def calculate_average_cubic_weight(items):
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
