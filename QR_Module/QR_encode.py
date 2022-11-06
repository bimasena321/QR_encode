import os as a
import pyqrcode as QR
a.system("clear")
#dibuat oleh bimasena321
def en_QR(a):
  print("tulis terserah km!!")
  b = input("buat barcode: ")
  kode = QR.create(b)
  kode.png("QR_kode.png",scale=10)
  a.system("mv QR_kode.png png_QR")
  print("QR code status: sukses")
  
  
  
  
  
  
  
