import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)


image = qr.make_image(fill_color='black', back_color='white')


image.save(filename)
print(f'QR code saved as {filename}')


'https://eclectic-bublanina-7d48d7.netlify.app/'