from PIL import Image

image = Image.open("monro.jpg")
print(image.mode) 
red, green, blue = image.split()
red.save("monrored.jpg")
green.save("monrogreen.jpg")
blue.save("monroblue.jpg")
