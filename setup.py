from setuptools import setup, find_packages

setup(
    name="genpypi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "setuptools>=42",
    ],
    entry_points={
        'console_scripts': [
            'genpypi=genpypi.cli:main',
        ],
    },
)