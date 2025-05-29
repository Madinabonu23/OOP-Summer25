import qrcode
url ="https://preview--madinabonu-warsaw-explorer.lovable.app/"
qr = qrcode.make(url)
qr.save("site_qr_kode.png")