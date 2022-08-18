import qrcode
# Link for website
input_data = "https://unicornstix.com"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill_color=(0,206,209), back_color='white')
img.save('qrcode-turquiose.png')