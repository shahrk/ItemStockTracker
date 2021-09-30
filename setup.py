from setuptools import setup

setup(
    name='ItemStockTracker',
    version='1.0.0',
    description='Tracks stock info from retailer websites',
    author='Qiuyu Chen, Yasitha Rajapaksha, Jiacheng Yang, Hugh Wright',
    author_email='qnchen@ncsu.edu, yrajapa@ncsu.edu, jyang31@ncsu.edu, jhwrigh2@ncsu.edu',
    url='https://github.com/qchen59/ItemStockTracker',
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
      keywords='',
      license='Apache-2.0 License',
      install_requires=[
        'pillow',
        'requests',
        'beautifulsoup4',
        'lxml',
        'setuptools',
        'sphinx',
        'sphinx-rtd-theme',
      ],
      )
