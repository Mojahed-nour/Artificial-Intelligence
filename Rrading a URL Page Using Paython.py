import requests
from bs4 import BeautifulSoup


def news():
    # the target we want to open
    url = 'https://sabq.org/'

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")


        print(resp.text)

    else:
        print("Error")


news()
