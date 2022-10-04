from matplotlib import image
import qrcode

data = 'QR Code using make() function'
img = qrcode.make(data)

img.save('primeiro_qrcode.png')