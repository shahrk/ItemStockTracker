from setuptools import setup

setup(
    name='ItemStockTracker',
    version='1.0.0',
    description='Tracks stock info from retailer websites',
    author='Krishna Saurabh Vankadaru, Rohan Prabhune, Swetha Gavini, Arjun Madhusudan, Ramya Sai Mullapudi',
    author_email='kvankad@ncsu.edu, rjprabhu@ncsu.edu,  lgavini@ncsu.edu, amadhus2@ncsu.edu, rmullap@ncsu.edu',
    url='https://github.com/ramyasaimullapudi/ItemStockTracker',
    packages=['code'],
      long_description="""\
        Module:
            * AmazonScraper
            * BestBuyScraper
            * GUI
            * Scraper
            * SendEmail
            * Tracker
      """,
    classifiers=[
        "License :: Apache-2.0 License",
        "Programming Language :: Python",
        "Development Status :: ",
        "Intended Audience :: Customers, Developers",
        "Topic :: D",
    ],
    keywords="",
    license="Apache-2.0 License",
    install_requires=[
        "pillow",
        "requests",
        "beautifulsoup4",
        "lxml",
        "setuptools",
        "sphinx",
        "sphinx-rtd-theme",
    ],
)
