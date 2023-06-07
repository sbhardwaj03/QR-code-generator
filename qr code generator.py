import pyqrcode
import png
link1= "https://www.instagram.com/the.clever.programmer/"
qr_code=pyqrcode.create(link1)
qr_code.png("instagram.png",scale=5)
