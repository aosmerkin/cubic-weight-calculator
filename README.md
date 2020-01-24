# Average Cubic Weight Calculator

This is a command line application that calculates average cubic weight of a specified category of items within a product catalog located somewhere on the web.

### Cubic Weight Example

A parcel measuring 40cm long (0.4m) x 20cm high (0.2m) x 30cm wide (0.3m) is equal to 0.024 cubic metres.
Multiplied by the conversion factor of 250 gives a cubic weight of 6kg. 

```bash
0.4m x 0.2m x 0.3m = 0.024m3
0.024m3 x 250 = 6kg
```

### Product Catalog API

The application expects that product catalog can be reached at the URL specified on command line and meets the following requirements:

* Product catalog can be queried via REST API endpoint `/api/products`
* Items in the catalog are returned grouped into pages. First page is accessible via `/api/products/1`
* Results on each page are presented in json format.
* Each page has _'next'_ field that contains a reference to the next page of products. The last page does not have this link.

Result page example:
```bash
> curl http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/1
{
    "objects": [
        {
            "category": "Category A",
            "title": "Car Sticker Decals",
            "weight": 120.0,
            "size": {
                "width": 15.0,
                "length": 13.0,
                "height": 1.0
            }
        },
        {
            "category": "Category B",
            "title": "Button Cell Battery",
            "weight": 60.0,
            "size": {
                "width": 5.8,
                "length": 19.0,
                "height": 0.3
            }
        },
        {
            "category": "Category C",
            "title": "Air Conditioner (2.9KW)",
            "weight": 26200.0,
            "size": {
                "width": 49.6,
                "length": 38.7,
                "height": 89.0
            }
        }
    ],
    "next": "/api/products/2"
}
```

# Design
Since the application shall handle catalogs of unspecified sizes it was chosen to use Python's generators to fetch data from the remote location.

All logic that interacts with the server is encapsulated into `calculator.api.Products` class.

`Products.pages()` generator allows to iterate over pages from the caller code almost as if the were normal list.

To further simplify interaction with the catalog there is `Products.items()` generator that allows to iterate over catalog items abstracting away from the notion of pages. In addition it allows to filter items that belong to a specific category. 

Average weight calculation is performed by `calculate_average_cubic_weight` function that accepts an iterable object. Items generator mentioned above is directly passed in there to provide access to catalog's items.


# Installation

## Simple way

1. Clone the project or unpack provided sources
2. Change into the project directory: `cd cubic-weight-calculator`
3. Execute `pip install .`

Now you shall be able to invoke the calculator:
```bash
cubic-weight-calculator \
    --url="http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com" \
    --category="Air Conditioners"
``` 


## Reproducible way

If you want to run the application in exactly the same environment as I did you may use pipenv:

1. Clone the project or unpack provided sources
2. Change into the project directory: `cd cubic-weight-calculator`
3. Install pipenv: `pip install pipenv`
4. Activate pipenv: `pipenv shell`
5. Install locked dependencies: `pipenv install --dev --deploy --ignore-pipfile`

Now you shall able to execute unit tests: 
```bash
python -m pytest --cov=calculator
```
Or run the application:
```bash
python -m calculator.main \
    --url="http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com" \
    --category="Air Conditioners"
``` 


If you want to be able to call the application using `cubic-weight-calculator` just execute `pip install .` when running inside pipenv shell.

## Lazy way

If you still want to run the application in the exact environment but do not want to rely on pipenv to manage your dependencies you may try a containerised version.

```bash
docker run --rm aosmerkin/cubic-weight-calculator --url="http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com" --category="Air Conditioners"
```


# Building docker image
There are two targets in Docker file which allow multi-stage builds.
* **prod** is used to create production images including only application code
* **dev** is designed to create images that could be used for testing and further development: it includes all required development dependencies. Default command is used to run unit tests.

## Creating and using production image
```bash
# Building image
docker build --target prod -t cubic-weight-calculator .

# Running application
docker run --rm cubic-weight-calculator --url="http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com" --category="Air Conditioners"
```

## Creating and using development image
```bash
# Building image
docker build --target dev -t cubic-weight-calculator-dev .

# Running tests 
docker run --rm cubic-weight-calculator-dev
```
