from PIL import Image


image = Image.open("monrogreen.jpg")


left =  100
right = image.width - 100
top = 0
coordinates = (left, top, right, image.height)
cropped = image.crop(coordinates)
cropped.save("monrogreen_middle.jpg")
image = Image.open("monrogreen_middle.jpg")
print(image.width)
print(image.height)