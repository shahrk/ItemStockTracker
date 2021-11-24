from setuptools import setup

setup(
    name="ItemStockTracker",
    version="2.1.0",
    description="Tracks stock info from retailer websites",
    author="Raj Shah, Nirav Patel, Parth Kanakiya, Mithil Dave, Bhargav Jethwa",
    author_email="rshah28@ncsu.edu, nkpatel8@ncsu.edu, pkanaki@ncsu.edu, mdave2@ncsu.edu, bjethwa@ncsu.edu",
    url="https://github.com/ramyasaimullapudi/ItemStockTracker",
    packages=["code"],
    long_description="""\
        Module:
            * AmazonScraper
            * BestBuyScraper
            * WalmartScraper
            * GUI
            * Scraper
            * SendEmail
            * Tracker
      """,
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python",
        "Development Status :: ",
        "Intended Audience :: Customers, Developers",
        "Topic :: D",
    ],
    keywords="",
    license="MIT License",
    install_requires=[
        "pillow",
        "requests",
        "beautifulsoup4",
        "lxml",
        "setuptools",
        "sphinx",
        "sphinx-rtd-theme",
        "tkinter",
    ],
)
