import pyqrcode as kodeQR
import os as a
QR = kodeQR.create("pesan:namaku bima sena w.p")
QR.png ("QRcodeQR.png",scale=7)
a.system("mv QRcodeQR.png arduino_python")
print ("QR_code dibuat : sukses ")
