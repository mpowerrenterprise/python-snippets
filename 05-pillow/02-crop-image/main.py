from PIL import Image

img = Image.open("img2.jpg")
area = (0,0,1500,1500) #The First two values are coordiates
copped_img = img.crop(area); #croped the IMG depanding on the vlaue of area
copped_img.show();#show it.