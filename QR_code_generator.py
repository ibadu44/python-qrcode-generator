import qrcode
data ="Ibad-ur-Rehman | Software Engineer | Python | ML | Data Engineer I'm Ibad-ur-Rehman, a passionate Software Engineer who transforms data into actionable insight"

qr=qrcode.make(data)

qr.save('qrcode.png')

print('QR code generated successfully!')