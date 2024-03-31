# Unstop-part2sub-solution
Scraping and Recommendation feature


# Scraping
using Selenium for web scraping, to scrape data from a table on a web page. 
need to install the Selenium package by running the command *pip install selenium* in a command prompt or terminal window.

Importing Driver:-
Selenium requires a web driver to interact with web pages
from selenium import webdriver
driver = webdriver.Chrome('/path/to/chromedriver')

# table_scraper.py
an example of using Selenium for web scraping, to scrape data from a table on a web page.


# job_scraper.py
Installing Required Libraries: Ensuring the necessary libraries installed. 
using pip to install libraries like BeautifulSoup, Selenium, and Pandas.
The following modules from the Selenium Library are used in this code: Webdriver, expected conditions, options, Keys, and sleep from time.

web scraping requires a web driver. we will use the Chrome browser, and the Chrome driver is downloaded from the internet.
# Set Up WebDriver:
Require Chrome WebDriver (chromedriver) executable in the same directory as of Python script or provide the correct path to it in the executable_path parameter when creating the WebDriver.

# Rayobyte
Rayobyte is a proxy vendor, they sell data center, residential and mobile proxies that can be used for scraping the web
we cannot make too many requests from the same IP address in a certain timeframe, otherwise we would be blocked.
That’s the main reason why proxy providers are used when it comes to web scraping.
