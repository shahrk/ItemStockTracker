# Item Stock Tracker
[![Build Status](https://github.com/ramyasaimullapudi/ItemStockTracker/workflows/Build%20Status/badge.svg)](https://github.com/ramyasaimullapudi/ItemStockTracker/actions)
[![Codestyle: Black](https://github.com/ramyasaimullapudi/ItemStockTracker/workflows/Black%20Format%20Checker/badge.svg)](https://github.com/ramyasaimullapudi/ItemStockTracker/actions)
[![codecov](https://codecov.io/gh/ramyasaimullapudi/ItemStockTracker/branch/main/graph/badge.svg?token=EHYPNZ5ACP)](https://codecov.io/gh/ramyasaimullapudi/ItemStockTracker)

![GitHub](https://img.shields.io/badge/language-python-blue.svg)
<a href="https://zenodo.org/badge/latestdoi/416888118"><img src="https://zenodo.org/badge/416888118.svg" alt="DOI"></a>
![GitHub](https://img.shields.io/github/license/shahrk/ItemStockTracker)
![lines of code](https://tokei.rs/b1/github/shahrk/ItemStockTracker?color=ff69b4&label=Lines%20of%20Code&style=flat-square)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/shahrk/ItemStockTracker)
![GitHub open issues](https://img.shields.io/github/issues/shahrk/ItemStockTracker)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/shahrk/ItemStockTracker)
![GitHub all downloads](https://img.shields.io/github/downloads/ramyasaimullapudi/ItemStockTracker/total)


# "Item Stock Tracker" is a program designed to alert users when specific items from an online retailer are back in stock.



https://user-images.githubusercontent.com/34405372/135356983-439e7808-8268-41aa-ad82-38615d4a773e.mp4



## Prerequisites
Make sure you have installed and followed all the following prerequisites on your development machine:

* Python-- [Download & Install Python 3.9](https://www.python.org/downloads/release/python-390/)
* Email-- Set environment variables for your email address(GMAIL_ID) and password(GMAIL_PASSWORD - you will have to use an [app password](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637730753160884408-1245442993&rd=1))
* pillow-- [Download & Install Pillow for python with version>=8.3.0](https://pillow.readthedocs.io/en/stable/)
* requests-- [Download & Install Requests for python with version~=2.26.0](https://docs.python-requests.org/en/latest/)
* beautifulsoup4-- [Download & Install Beautifulsoup4 for python with version~=4.10.0](https://pypi.org/project/beautifulsoup4/)
* lxml-- [Download & Install lxml for Python with version~=4.6.3](https://lxml.de)
* setuptools-- [Download & Install setuptools for Python with version~=57.0.0](https://pypi.org/project/setuptools/)
* sphinx-- [Download & Install setuptools for Python with sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
* sphinx-rtd-theme-- [Download & Install setuptools for Python with sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/)

### Documentation
[Item Stock Tracker’s documentation](https://itemstocktracker1.readthedocs.io/en/latest/)

### Installation

1. Download the latest [release](https://github.com/ramyasaimullapudi/ItemStockTracker/releases/) from the repository based on your operating system.

2. Extract the zip file downloaded.

3. Run ItemStockTracker.exe from the extracted folder to launch the application.

### Build executable 

To build the executable, you need to have pyinstaller installed which can be done using `pip install pyinstaller`. 
Navigate to `ItemStockTracker` folder and run the below commands based on the operating system you are running.

For Windows 

`pyinstaller --distpath ./build/dist --workpath ./build/build --noconfirm ./ItemStockTracker.spec`

For Mac

`pyinstaller  --distpath ./build/dist --workpath ./build/build --noconfirm ./ItemStockTrackerMac.spec`

The executable will be found in the folder</br>
`ItemStockTracker/build/dist/ItemStockTracker/ItemStockTracker.exe` for windows</br>
`ItemStockTracker/build/dist/ItemStockTrackerMac/ItemStockTrackerMac` for MacOS

To run the app on MacOS execute the following commands from the project's base directory:  
`cd ItemStockTracker/build/dist/ItemStockTrackerMac`  
`./ItemStockTrackerMac`


---
## Usage


![image](https://user-images.githubusercontent.com/19464321/140402539-b528fbaa-b352-454d-96ae-a9af6b01f623.png)

By default, the GUI will already contain some data, which is loaded from `data/tracker.txt`. To add your own items, click the plus button in the upper right. You will be prompted to enter a name for the item you are tracking, along with a URL for a specific product page. Currently, `amazon.com`, `bestbuy.com` and `walmart.com` product pages are supported.
  
![7](https://user-images.githubusercontent.com/51504486/140412693-de447000-4c6e-47c8-88da-f31ffc6b1c6d.PNG)

You can also edit, add, or delete items by right-clicking on a selected item,
  
![8](https://user-images.githubusercontent.com/51504486/140413151-fa73f2fc-adde-4f8a-ae91-1e95f06a6dce.PNG)

When an item is restocked, a popup will appear. Aditionally, a system notification will also be generated 
  
  ![image](https://user-images.githubusercontent.com/30803969/134995936-a4088c47-229a-43cf-b01d-a9ae6e787b7b.png) ![5](https://user-images.githubusercontent.com/51504486/140413777-9632cd0b-9a50-48f6-874b-6cf8fb40c0a4.PNG)
  
In the "Settings" tab you have the following functionalities:

![2](https://user-images.githubusercontent.com/51504486/140414731-4015eae0-f7ff-4509-af19-57823fd76c07.PNG)


- Adjust the refresh interval - How often you want to poll the website to check the status of your items
- Configure your email alert settings - Want an email alert ? Just tick the checkbox and enter your email address
- Minimize to system tray - Don't want to see the window in the taskbar ? Just minimize it to system tray. You will see a plus sign:

 ![4](https://user-images.githubusercontent.com/51504486/140416010-67519366-eed6-41a1-8b87-6cb9f51639b4.PNG)
- Launch tracker at startup - If you want to start checking the stock status of your items automatically on system startup 


Lastly, all the info about our application can be found out in newly added INFO tab.
![3](https://user-images.githubusercontent.com/51504486/140417132-3c0963de-d507-465b-8721-f397e5645a71.PNG)


---
## Improvements over previous versions Project2:
1. Extended functionality of the application by supporting new websites that can be tracked like walmart.
2. Since cost is also a major factor for making the purchase decision we added a column to show the current price of the item without constantly checking the websites saving lot of time when comparing between different websites.
3. Enhanced deployment by creating an executable file that can be installed on both Windows and MacOS
4. In the prior implementation the availability notification was a pop-up which might be missed if the application is minimized. We have integrated the notifications to the system for both Windows and MacOS
5. Implemented auto launch during system startup, limited to Windows OS.
6. We have added a functionality to minimize the application to system tray.
7. Added Black and github actions to automatically check for formatting errors and run test cases for each commit.
8. Multithreaded scrapers to run parallely using thread pools to fetch stock availability and prices.
9. Improved documentation in code, also providing clear instructions on setup and getting started.

---
## Improvements over previous versions Project3: 

Please find the detailed report on Enhancement work done by our team here : https://github.com/shahrk/ItemStockTracker/blob/main/docs/Proj3Enhancement.pdf
1. Price Drop Alert : If a user wants to purchase certain products but wants to wait until the price is lowered, they can make use of our brand new “Price Drop Alert” feature.  
2. Item Restock Alert: For out of stock items, users no longer have to check the webpages again and again. Our new feature will give users an item stock alert which will save their time.
3.Show Discounted Price : Earlier the scraper was fetching the real price of the product rather than the discounted price. Now if the e-commerce website adds new discounted prices, it will be shown on our dashboard. Earlier it was throwing a null value error.
4. Amazon Scraper: We added a new scrapper for Amazon. Earlier we had scrapers for BestBuy and Walmart. The new Scrapper will help the users to track items from Amazon webpage. 
5. UI Enhancement: We created a new Web based app for our project. The desktop version was tedious to install and maintain. It is much better for users to have a web-based version. We created a simple UI where users can log in and add items to track. They will be notified via email if/when the stock/price of the products they add changes.
6. Bug Fix 1(App not working when notification is triggered): When we downloaded the project initially, we found that there was a major error in the functioning of the triggers. The GUI stops refreshing whenever the notification is triggered. The error message was shown in the console whenever notifications are pushed via trigger. 
7. Bug Fix 2(The support for MAC OS): The app was not deployable on  mac os. There were several complications arising due to the Application initially developed using Windows. We also added the automatic homebrew installation script in the fix. 
The fix is been provided in this commit: 
8. Bug Fix 3(Fixed SendEmail.py): Earlier, the code was using hardcoded email id/password to send price alerts. This now is fixed and now it sends the alerts using environmental IDs. 
9. Added new tools: We added new code coverage, line counter, code style checker and code formatter tools. We used pylint for performing code style checks. We used Black Formatter for checking code format. 

---
## Future Goals
- We can suggest price compare for different products to the users where they will be shown the prices of the same product on the various paltforms. The User can then select the best website to purchase that item. 
- We can havbe more supported retailers. For example, Nike.com, GAP.com, eabay.com etc. 
- Item dashboard: This item dashboard will show the basic information of the products including the size/color etc. User can choose to track speciifc product based on size and color. 
- Add Machine Learning: We can analyze and predict the prices in future using machine learning so that user can choose to wait until they gets their expected prices.   


---
## Questions?
If you encountered any questions and seeking for helps, please reach out to us at
<br/>[SEGroup27.2021@gmail.com](mailto:featurehuntteam@gmail.com)
<br/>Alternatively, you can contact any of the team members listed below.

---
## Team Members



<table>
  <tr>
    <td align="center"><a href="https://github.com/shahrk/"><img src="https://avatars.githubusercontent.com/u/11090612?v=4" width="100px;" alt=""/><br /><sub><b>Raj Shah</b></sub></a></td>
    <td align="center"><a href="https://github.com/Nirav1929/"><img src="https://avatars.githubusercontent.com/u/11133468?v=4" width="100px;" alt=""/><br /><sub><b>Nirav Patel</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Parth59/"><img src="https://avatars.githubusercontent.com/u/22288099?v=4" width="100px;" alt=""/><br /><sub><b>Parth Kanakiya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/mithildave/"><img src="https://avatars.githubusercontent.com/u/26930183?v=4" width="100px;" alt=""/><br /><sub><b>Mithil Dave</b></sub></a><br /></td>
    <td align="center"><a href="https://www.github.com/BhargavJethwa"><img src="https://avatars.githubusercontent.com/u/70560970?v=4" width="100px;" alt=""/><br /><sub><b>Bhargav Jethwa</b></sub></a><br /></td>
  </tr>
</table>

