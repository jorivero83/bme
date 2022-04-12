from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # Package name:
    name="bme",

    # Package number (initial):
    version="0.1.0",

    # Package author details:
    author="Jorge Rivero Dones",
    author_email="jorivero83@gmail.com",

    # Packages
    packages=["bme"],

    # Include additional files into the package
    include_package_data=False,

    # Details
    url="https://github.com/jorivero83/bme_data",

    #
    # license="LICENSE.txt",
    description="A package to download data from www.bolsamadrid.es",

    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',

    # Dependent packages (distributions)
    install_requires=[
        "bs4",
        "lxml",
        "tqdm",
        "pandas"
    ],
)