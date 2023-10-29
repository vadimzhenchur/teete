from PIL import Image
from PIL import ImageFilter

with  Image.open('Coka-Cola.jpg') as pic_original:
    pic_blured = pic_original.filter(ImageFilter.GaussianBlur(5))
    pic_blured.save('blured.jpg')
    pic_blured.show()