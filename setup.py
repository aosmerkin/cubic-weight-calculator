from setuptools import setup

setup(
    name='cubic-weight-calculator',
    version='0.1.0',
    packages=['calculator'],
    entry_points={
        'console_scripts': [
            'cubic-weight-calculator = calculator.main:main'
        ]
    },
    install_requires=[
        "requests",
        "click"
    ]
)
