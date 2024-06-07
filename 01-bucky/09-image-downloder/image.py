import random
import urllib.request

def downloadImage(url):
    urlname=random.randrange(1,1000)
    urlextension=str(urlname)+ ".jpg"
    urllib.request.urlretrieve(url,urlextension)

downloadImage("https://www.ophtek.com/wp-content/uploads/2014/08/java_tech-540x405.jpg")