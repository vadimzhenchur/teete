from PIL import Image

with  Image.open('Coka-Cola.jpg') as pic_original:
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print('Зображення відкрито\n Розмір:' , pic_gray.size)
    print('', pic_gray.format)
    print('', pic_gray.mode)
    pic_gray.show()