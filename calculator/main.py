import click
from .api import Products
from .functions import calculate_average_cubic_weight
from .errors import AppError


@click.command()
@click.option('--url', required=True, type=str, help='Product catalog URL')
@click.option('--category', required=True, type=str, help='Product category')
def main(url, category):
    try:
        products = Products(url)
        result = calculate_average_cubic_weight(products.items(category))
        if result != 0:
            print(f"Average Cubic Weight is {result} kg")
        else:
            print("Calculated weight is 0: It is likely that there are no products in the selected category.")
    except AppError as e:
        print(e)


if __name__ == '__main__':
    main()
