from PIL import Image

image = Image.open("monroblue.jpg")
left =  0
right = image.width - 200
top = 0
coordinates = (left, top, right, image.height)
cropped = image.crop(coordinates)
cropped.save("monroblue_right.jpg")