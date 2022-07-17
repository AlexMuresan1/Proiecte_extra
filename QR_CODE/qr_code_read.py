import cv2

img=cv2.imread("qrcode.png")
detector=cv2.QRCodeDetector()
data,bbox,straight_qrcode=detector.detectAndDecode(img)
print("Site:",data)
