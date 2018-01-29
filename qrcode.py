from PIL import Image
from pyzbar.pyzbar import decode

decoded = decode(Image.open('qr.jpg'))
print(decoded)

url = 'https://u.wechat.com/EE1b50ITmTp4JuL4Hh3ktAQ'