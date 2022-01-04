from distutils.core import setup

setup(
    # Application name:
    name="ffin",

    version="0.0.1",

    author="Francisco Vicente",
    author_email="fvpan01@gmail.com",

    # Packages
    packages=["ffin"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/Fadta/ffin",

    #
    license="LICENSE",
    # description="",

    # long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pandas",
        "yfinance",
        "pandas_ta",
    ],

    entry_points={
        "console_scripts": [
        ],
    }
)
