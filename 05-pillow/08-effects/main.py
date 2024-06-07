from PIL import Image
from PIL import ImageFilter

TheImage = Image.open("img1.jpg") #This is Image
blur = TheImage.filter(ImageFilter.BLUR)
detail = TheImage.filter(ImageFilter.DETAIL)
edg = TheImage.filter(ImageFilter.FIND_EDGES)
blur.show()
detail.show()
edg.show()