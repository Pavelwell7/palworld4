from PIL import Image

red = Image.open("monrored2.jpg") 
blue = Image.open("monroblue2.jpg")
green = Image.open("monrogreen_middle.jpg")

new_image = Image.merge("RGB", (red, blue, green,))
new_image.save("finalmonro2.jpg")