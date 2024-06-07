import requests
from bs4 import BeautifulSoup

def trade_spider():

    url = 'https://www.w3schools.com'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a',{'class':'w3-bar-item'}):
        style=link.get('href')
        print(style)


trade_spider()


