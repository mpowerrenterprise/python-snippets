from PIL import Image

mainImg = Image.open("img1.jpg")
headImg = Image.open("head.png")

area = (800,300)
mainImg.paste(headImg,area)

mainImg.show()


