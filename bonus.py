import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter


files = os.listdir("photos")
with  Image.open('Coka-Cola.jpg') as pic_original:
    pic_blured = pic_original.filter(ImageFilter.GaussianBlur(5))
    pic_blured.save('blured.jpg')
    pic_blured.show()
for photo in files:
    with Image.open("photos/"+ photo) as image:
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("MADE TheArtist Script PERSONAL USE.otf", 100)

        draw.text((10,10), "Coca-Cola", font=font, fill="white")

        image.save("result/"+photo)

