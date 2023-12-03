from PIL import Image
with  Image.open('Coka-Cola.jpg') as pic_original:
    print('Зображення відкрито\n Розмір:' , pic_original.size)
    print('', pic_original.format)
    print('', pic_original.mode)
    pic_original.show()