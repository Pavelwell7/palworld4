from PIL import Image

image1 = Image.open("monroblue_right.jpg")
image2 = Image.open("monroblue_middle.jpg")
image3 = Image.blend(image1, image2, 0.5)
image3.save("monroblue2.jpg")