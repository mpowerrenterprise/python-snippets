from PIL import Image


TheImage = Image.open("img1.jpg") #This is Image
out_put = TheImage.convert("L")   #To black and White
out_put.show()