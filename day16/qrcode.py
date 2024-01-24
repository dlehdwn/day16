import qrcode

url = 'https://www.instagram.com/riize_official/'
img = qrcode.make(url)
img.save('./riize.png')