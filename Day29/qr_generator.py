import qrcode

url = input("Enter the URL: ")
path = "qrcode.png"

qr = qrcode.QRCode()   # fixed: QRCode, not QRcode
qr.add_data(url)
qr.make(fit=True)      # added: this actually builds the QR matrix from the data

img = qr.make_image(fill_color="black", back_color="white")
img.save(path)

print(f"QR code saved as {path}")