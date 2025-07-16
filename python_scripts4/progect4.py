from PIL import Image

image = Image.open("monrored.jpg")
coordinates = (100, 0, image.width - 100, image.height)
cropped = image.crop(coordinates)
cropped.save("monrored_middle.jpg")  
