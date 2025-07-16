from PIL import Image

image = Image.open("example.jpg")
print(image.mode)  
red, green, blue = image.split()  
new_image = Image.merge("RGB", (red, green, blue))
new_image.save("monroreturn.jpg")