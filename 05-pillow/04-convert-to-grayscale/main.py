from PIL import Image

TheImage = Image.open("img1.jpg")
r,g,b = TheImage.split()

r.show()
g.show()
b.show()

#This program gets the primary color of the image
