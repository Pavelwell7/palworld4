from PIL import Image

image = Image.open("finalmonro.jpg")
print(image.size)   
image.thumbnail((80, 80))  
print(image.size)  
image.save("finalmonrosmall.jpg")