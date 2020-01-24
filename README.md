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
