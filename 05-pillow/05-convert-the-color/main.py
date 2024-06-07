from PIL import Image

TheImage = Image.open("img1.jpg")
r,g,b = TheImage.split()
new_img = Image.merge("RGB",(g,r,r))
new_img.show()
new_img.save("new_img.jpg")