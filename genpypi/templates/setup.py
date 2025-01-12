from setuptools import setup, find_packages

setup(
    name="{{ package_name }}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="",  # Add your name
    author_email="",  # Add your email
    description="",  # Add short description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/{{ package_name }}",  # Update with your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 