import qrcode

#generating QR CODE

site="https://www.utcluj.ro"
cod=qrcode.make(site)
cod.save("qrcode.png")
