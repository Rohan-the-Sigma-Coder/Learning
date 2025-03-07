import qrcode
text_or_file = input('Enter the text or URL: ')
filename = input('Enter the filename: ')
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4  )  
data = text_or_file
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill = 'black', back_color = 'white')
img.save(filename)

print(f'QR code saved as {filename}')