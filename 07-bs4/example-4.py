import  requests
import urllib.request
import random
import os
from bs4 import BeautifulSoup

def webisteDownloader(maxPage):
    page = 1
    number = 0
    while page <= maxPage:
        url='http://wallpaperswide.com/computers-desktop-wallpapers/page/' +str(page)
        source_code = requests.get(url)    #Get the source_code of the page.
        text_code = source_code.text       #Converted into text.
        bs4Method = BeautifulSoup(text_code,"html.parser")        #Converted as the BeautifulSoup Object.
        for link in bs4Method.findAll('img', {'class': 'thumb_img'}):
            style = link.get('src')
            name=str(number)+'.jpg'
            number+=1
            newFolder=r'images/'
            if not os.path.exists(newFolder):
                os.mkdir(newFolder)
            urllib.request.urlretrieve(style,newFolder+name)
        page +=1



numbers= input("Enter the how many pages do you want to download ")
webisteDownloader(int(numbers))

