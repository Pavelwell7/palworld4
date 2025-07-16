from PIL import Image

image = Image.open("monroblue.jpg")
left =  100
right = image.width - 100
top = 0
coordinates = (left, top, right, image.height)
cropped = image.crop(coordinates)
cropped.save("monroblue_middle.jpg")