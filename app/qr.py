import qrcode
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(version=1, error_correction=ERROR_CORRECT_H,
                   box_size=20, border=4)
qr.add_data("https://www.linkedin.com/in/swasthik-r-prabhu-644607258/")
qr.make(fit = True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("Qrcode.png")