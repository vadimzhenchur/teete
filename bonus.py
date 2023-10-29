import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter


files = os.listdir("photos")

for photo in files:
    with Image.open("photos/"+ photo) as image:
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("MADE TheArtist Script PERSONAL USE.otf", 100)

        draw.text((10,10), "Coca-Cola", font=font, fill="white")

        image.save("result/"+photo)

