from PIL import Image

TheImage = Image.open("img1.jpg") #This is Image

sq = TheImage.resize((200,200))   #Here we resize the image.
f_b=TheImage.transpose(Image.FLIP_TOP_BOTTOM) #flip the image
spin=TheImage.transpose(Image.ROTATE_90)      #rotate

f_b.show() 
sq.show()
spin.show()