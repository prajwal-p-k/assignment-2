from PIL import Image

# Open an image file
image = Image.open('path_to_image.jpg')
new_image = image.resize((new_width, new_height))
left, upper, right, lower = 100, 100, 300, 300
cropped_image = image.crop((left, upper, right, lower))
rotated_image = image.rotate(90)  # rotates the image by 90 degrees
flipped_horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
grayscale_image = image.convert('L')

from PIL import ImageFilter

blurred_image = image.filter(ImageFilter.BLUR)
sharpened_image = image.filter(ImageFilter.SHARPEN)
new_image.save('new_path_to_save.jpg', 'JPEG')

from PIL import ImageDraw

draw = ImageDraw.Draw(image)
draw.line((0, 0) + image.size, fill=128)
draw.line((0, image.size[1], image.size[0], 0), fill=128)

from PIL import ImageFont

font = ImageFont.truetype("path_to_font.ttf", 30)
draw.text((10,10), "Hello World", font=font, fill="white")

background = Image.open('path_to_background.jpg')
foreground = Image.open('path_to_foreground.png')

background.paste(foreground, (x, y), foreground)  # the last parameter is the alpha mask for transparency
