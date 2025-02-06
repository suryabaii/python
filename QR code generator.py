import qrcode
data = input('Enter the URL:').strip()
file= input('FileName:').strip()
su=qrcode.QRCode(box_size=10 , border=5)
su.add_data(data)
image= su.make_image( fill_color='black',back_color='white')
image.save(file)
print (f'Qr Saved as{file}')