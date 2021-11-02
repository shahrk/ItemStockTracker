# Item Stock Tracker
[![Build Status](https://github.com/ramyasaimullapudi/ItemStockTracker/workflows/Build%20Status/badge.svg)](https://github.com/ramyasaimullapudi/ItemStockTracker/actions)
[![Coverage Status](https://coveralls.io/repos/github/qchen59/ItemStockTracker/badge.svg?branch=main)](https://coveralls.io/github/qchen59/ItemStockTracker?branch=main)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ramyasaimullapudi/ItemStockTracker)
![GitHub open issues](https://img.shields.io/github/issues/ramyasaimullapudi/ItemStockTracker)
![GitHub all downloads](https://img.shields.io/github/downloads/ramyasaimullapudi/ItemStockTracker/total)
<a href="https://zenodo.org/badge/latestdoi/416888118"><img src="https://zenodo.org/badge/416888118.svg" alt="DOI"></a>
[![codecov](https://codecov.io/gh/ramyasaimullapudi/ItemStockTracker/branch/main/graph/badge.svg?token=EHYPNZ5ACP)](https://codecov.io/gh/ramyasaimullapudi/ItemStockTracker)


# "Item Stock Tracker" is a program designed to alert users when specific items from an online retailer are back in stock.



https://user-images.githubusercontent.com/34405372/135356983-439e7808-8268-41aa-ad82-38615d4a773e.mp4



### Prerequisites
Make sure you have installed and followed all of the following prerequisites on your development machine:

* Python-- [Download & Install Python 3.9](https://www.python.org/downloads/release/python-390/)
* Email-- Fill out the email address(gmail_user) and password(gmail_password) in SendEmail.py as the sender email
* pillow-- [Download & Install Pillow for python with version>=8.3.0](https://pillow.readthedocs.io/en/stable/)
* requests-- [Download & Install Requests for python with version~=2.26.0](https://docs.python-requests.org/en/latest/)
* beautifulsoup4-- [Download & Install Beautifulsoup4 for python with version~=4.10.0](https://pypi.org/project/beautifulsoup4/)
* lxml-- [Download & Install lxml for Python with version~=4.6.3](https://lxml.de)
* setuptools-- [Download & Install setuptools for Python with version~=57.0.0](https://pypi.org/project/setuptools/)
* sphinx-- [Download & Install setuptools for Python with sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
* sphinx-rtd-theme-- [Download & Install setuptools for Python with sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/)

### Documentation
[Item Stock Tracker’s documentation](https://htmlpreview.github.io/?https://github.com/qchen59/ItemStockTracker/blob/main/docs/build/html/index.html)

### Installation

1. Download the project from GitHub or clone the repository.

`git clone https://github.com/qchen59/ItemStockTracker.git`



<img width="714" alt="Screen Shot 2021-10-06 at 3 30 28 AM" src="https://user-images.githubusercontent.com/34405372/136159116-5de09c46-95ac-4531-ada6-d14933d41478.png">

2. Change the current directory to the project folder, install the required packages.

`cd ItemStockTracker`

`pip install -r requirements.txt`

3. Change the current directory to `code`, then run the `GUI.py`.

`cd code`

`python3 GUI.py`


### Usage


![image](https://user-images.githubusercontent.com/30803969/134994728-681060a5-626a-4f5b-85b1-0936a7a9a697.png)

By default, the GUI will already contain some data, which is loaded from `data/tracker.txt`. To add your own items, click the plus button in the upper right. You will be prompted to enter a name for the item you are tracking, along with a URL for a specific product page. Currently, `amazon.com` and `bestbuy.com` product pages are supported.
  
![image](https://user-images.githubusercontent.com/30803969/134995508-7de37397-a552-4af9-82aa-94f13aca6830.png)

You can also edit, add, or delete items by right-clicking on a selected item:
  
  ![image](https://user-images.githubusercontent.com/30803969/134995597-1460417a-a0df-42d4-92a9-c0c0802fa67b.png)

When an item is restocked, a popup will appear. Optionally, an email alert will also be sent to a specified address.
  
  ![image](https://user-images.githubusercontent.com/30803969/134995936-a4088c47-229a-43cf-b01d-a9ae6e787b7b.png)
  
Lastly, in the "Settings" tab you can adjust the refresh interval (how often the program will poll the website to check the stock status of your items), and configure your email alert settings.

  ![image](https://user-images.githubusercontent.com/30803969/134995891-10801bc1-8d94-44be-8e01-1f4bd80fb68d.png)
  

All the info about our application can be found out in newly added INFO tab.

### Future Goals
- Collect the in-stock drop data and predict the next drop time.
- More supported retailers.
- [Other enhancements](https://github.com/qchen59/ItemStockTracker/issues)



### Questions?
If you encountered any questions and seeking for helps, please contact the following emails.
rmullap@ncsu.edu, rjprabhu@ncsu.edu, amadhur2@ncsu.edu, lgavini@ncsu.edu, kvankad@ncsu.edu

### Team Members
Arjun Madhusudan </br>
Ramya Sai Mullapudi </br>
Lakshmi Swetha Gavini </br>
Rohan Prabhune </br>
Saurabh Krishna </br>
