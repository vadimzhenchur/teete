from PIL import Image, ImageEnhance
from PIL import ImageFilter
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *

import os


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


app = QApplication([])
window = QWidget()
window.resize(800, 500)
mainLine = QHBoxLayout()
Non = QHBoxLayout()
window.setStyleSheet(
    """
    QPushButton:hover {
         background-color: Red
         }
         """
)
app.setStyleSheet("""
     QWidget{
          background-color: #F54545;
          
          }
     
     QPushButton{

        background-color: #CD5C5C;
        border-width: 3px;
        border-color: red yellow green hsla(60, 90%, 50%, .8);
        border-style: inset;
        font-family: Gill Sans;
        font-weight: bolder;
        font-feature-settings: smcp;
        min-width: 10em;
        padding: 10px;
        border-radius: 10px;
        color: Blue;
        transform: scale(0.5) translate(-100%, -100%);

        }
     QGroupBox {
        border-style: inset;
        border-width:10px;
        border-color: red yellow green hsla(60, 90%, 50%, .8);
        border-radius: 10px;
        font-family: Gill Sans;
        font-weight: bolder;
        font-feature-settings: smcp;
        transform: scale(0.5) translate(-100%, -100%);
        }
       
        QSpinBox {
        border-style: inset;
        border-width: 10px;
        border-color: red yellow green hsla(60, 90%, 50%, .8);
        border-radius: 10px;
        font-family: Impact;
        font-weight: bolder;
        font-feature-settings: smcp;
        transform: scale(0.5) translate(-100%, -100%);
        }
       
        
          """)

windows1 = QLabel("ПАПКА")
windows2 = QLabel("АБОНЕНТ")
windows3 = QLabel("НОМЕР")
windows4 = QLabel("РІДНИЙ")
windows5 = QLabel("КОЛЄГА")
windows6 = QLabel("БАТЬКІВЩИНА")
windows7 = QLabel("НОМЕРОГРАМ")
mono1 = QPushButton("ПАПКА")
mono2 = QPushButton("Вліво")
mono3 = QPushButton("Вправо")
mono4 = QPushButton("Дзеркало")
mono5 = QPushButton("ТИСНЕННЯ")
mono6 = QPushButton("Ч/Б")
mono7 = QPushButton("+ЯСКР")
mono8 = QPushButton("-ЯСКР")
mono9 = QPushButton("+КОНТ")
mono10 = QPushButton("-КОНТР")
mono11 = QPushButton("НАКЛ/КОНТР")
mono12 = QPushButton("НАЗАД")
text = QListWidget()
Mon = QVBoxLayout()
Mon.addWidget(mono1)
Mon.addWidget(text)
mainLine.addLayout(Mon)
Mon1 = QVBoxLayout()
Mon1.addWidget(windows7)

Non1 = QHBoxLayout()
Non.addWidget(mono2)
Non.addWidget(mono3)
Non.addWidget(mono4)
Non.addWidget(mono5)
Non.addWidget(mono6)
Mon1.addLayout(Non)

Non2 = QHBoxLayout()
Non2.addWidget(mono7)
Non2.addWidget(mono8)
Non2.addWidget(mono9)
Non2.addWidget(mono10)
Non2.addWidget(mono11)
Mon1.addLayout(Non2)
mainLine.addLayout(Mon1)

Non3 = QHBoxLayout()
Non3.addWidget(mono12)
Mon1.addLayout(Non3)
mainLine.addLayout(Mon1)


class WorkPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filename = None
        self.images = []

    def load(self):
        imagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(imagePath)
        self.images.append(self.image)

    def showImage(self):
        pixel = pil2pixmap(self.images[-1])
        pixel = pixel.scaled(800, 600, Qt.KeepAspectRatio)

        windows7.setPixmap(pixel)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.images.append(self.image)

        self.showImage()

    def rotate_ridth(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.images.append(self.image)

        self.showImage()

    def blackwhite(self):
        self.image = self.image.convert("L")
        self.images.append(self.image)

        self.showImage()

    def reflection(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.images.append(self.image)

        self.showImage()

    def pressing(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.images.append(self.image)

        self.showImage()

    def brightness1(self):
        self.image = ImageEnhance.Brightness(self.image).enhance(1.5)
        self.images.append(self.image)

        self.showImage()

    def brightness2(self):
        self.image = ImageEnhance.Brightness(self.image).enhance(0.9)
        self.images.append(self.image)

        self.showImage()

    def contrast1(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.5)
        self.images.append(self.image)

        self.showImage()

    def contrast2(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(0.9)
        self.images.append(self.image)

        self.showImage()

    def overlayingcontours(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.images.append(self.image)

        self.showImage()

    def nazad(self):
        self.images.pop()
        self.showImage()


workwithphoto = WorkPhoto()
mono2.clicked.connect(workwithphoto.rotate_left)
mono3.clicked.connect(workwithphoto.rotate_ridth)
mono6.clicked.connect(workwithphoto.blackwhite)
mono4.clicked.connect(workwithphoto.reflection)
mono5.clicked.connect(workwithphoto.pressing)
mono7.clicked.connect(workwithphoto.brightness1)
mono8.clicked.connect(workwithphoto.brightness2)
mono9.clicked.connect(workwithphoto.contrast1)
mono10.clicked.connect(workwithphoto.contrast2)
mono11.clicked.connect(workwithphoto.overlayingcontours)
mono12.clicked.connect(workwithphoto.nazad)


def open_folder():
    workwithphoto.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(workwithphoto.folder)
    text.clear()
    text.addItems(files)


def showChosenImage():
    workwithphoto.filename = text.currentItem().text()
    workwithphoto.load()
    workwithphoto.showImage()


text.currentRowChanged.connect(showChosenImage)
mono1.clicked.connect(open_folder)
window.setLayout(mainLine)
window.show()
app.exec()
