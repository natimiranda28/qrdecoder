import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Generar un código QR
data = "https://www.ejemplo.com"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("codigo_qr.png")

# Leer un código QR desde una imagen
qr_code = Image.open("codigo_qr.png")
decoded_data = decode(qr_code)
print(decoded_data[0].data.decode('utf-8'))