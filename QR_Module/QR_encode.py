import os as a
import pyqrcode as QR
a.system("clear")
#dibuat oleh bimasena321
def en_QR(a):
  print("""
  =============================
  = created by bimasena321    =
  = hasil ada di folder pngQR =
  = ketik terserah anda!!     =
  =============================
  """)
  b = input("buat barcode: ")
  kode = QR.create(b)
  kode.png("QR_kode.png",scale=10)
  a.system("mv QR_kode.png pngQR")
  print("QR code status: sukses")
  
  
  
  
  
  
  
