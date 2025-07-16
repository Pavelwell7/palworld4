from PIL import Image

image = Image.open("monrored.jpg")
coordinates = (200, 0,  image.width, image.height)
cropped = image.crop(coordinates)
cropped.save("monrored_left.jpg")  
