from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

red_cropped1 = red.crop((200, 0,  red.width, red.height))
red_cropped2 = red.crop((100, 0, image.width - 100, image.height))
red_blend = Image.blend(red_cropped1, red_cropped2, 0.5)

left =  0
right = image.width - 200
top = 0
blue_cropped1 = blue.crop((left, top, right, image.height))
left2 =  100
right2 = image.width - 100
top = 0
blue_cropped2 = blue.crop((left2, top, right2, image.height))
blue_blend = Image.blend(blue_cropped1, blue_cropped2, 0.5)


left3 =  100
right3 = image.width - 100
top = 0
green_cropped = green.crop((left3, top, right3, image.height))

new_image = Image.merge("RGB", (red_blend, blue_blend, green_cropped))
new_image.save("finalmonro4.jpg")

new_image.thumbnail((80, 80)) 
new_image.save("finalmonrosmall4.jpg")