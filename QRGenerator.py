import pyqrcode
from PIL import Image, ImageDraw, ImageFont

url = 'https://www.linkedin.com/in/jian-zhi-wong-837858175/'
qr = pyqrcode.create(url)
#qr.png('QR.png', scale=10)

with open('QR.png', 'wb') as f:
	qr.png(f, scale=10)

im = Image.open('QR.png')
width, height = im.size
logo_size = 100
#logo = Image.open('in.png')

logo = Image.new('RGB', (logo_size,logo_size), color = (14,118,168))
font = ImageFont.truetype('/mnt/c/Windows/Fonts/timesbd.ttf', 72)
d = ImageDraw.Draw(logo)
d.text((20,10), 'in', font=font, fill=(255,255,255))

xmin = ymin = int((width/2) - (logo_size/2))
xmax = ymax = int((width/2) + (logo_size/2))

#logo = logo.resize((xmax - xmin, ymax - ymin))
im.paste(logo, (xmin, ymin, xmax, ymax))
im.save('QRwithPic.png')
import pyqrcode
from PIL import Image, ImageDraw, ImageFont

url = 'https://www.linkedin.com/in/jian-zhi-wong-837858175/'
qr = pyqrcode.create(url)
qr.png('QR.png', scale=10)

im = Image.open('QR.png')
im = im.convert('RGBA')
width, height = im.size
logo_size = 100

logo = Image.new('RGBA', (logo_size,logo_size), color = (14,118,168))
font = ImageFont.truetype('/mnt/c/Windows/Fonts/timesbd.ttf', 72)
d = ImageDraw.Draw(logo)
d.text((20,10), 'in', font=font, fill=(255,255,255))

xmin = ymin = int((width/2) - (logo_size/2))
xmax = ymax = int((width/2) + (logo_size/2))

im.paste(logo, (xmin, ymin, xmax, ymax))
im.save('QRwithPic.png')
