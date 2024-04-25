import segno
import cv2
from pyzbar import pyzbar


def makeqr():
    while True:
        link = str(input("Write link or any text for make QR Code > "))
        qrcode = segno.make(link, micro=False)
        qrcode.save("qrcode.png", scale=6)

        print("Done! I save your QR Code in qrcode.png")

        open_qr = str(input("open QR or exit? > "))
        if open_qr == "open":
            qrcode.show()
            print("Bye Bye!")
            break
        elif open_qr == "exit":
            print("Bye Bye!")
            break
        else:
            print("WRITE ONLY open OR exit :)")
            makeqr()

def decodeqr():
    while True:
        qrlink = str(input("Link to QR Code file > "))
        img = cv2.imread(qrlink)
        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
            qrdata = barcode.data.decode("utf-8")
            print(f"Result: {qrdata}")
        
        print("You want decode more QR? (Yes or No)")
        quas = str(input(">> "))
        if quas == "Yes":
            decodeqr()
        else:
            break


def start():
    print("""What do you want?
    1) Make QR Code
    2) Decode QR code""")
    change = str(input(">> "))

    if change == "1":
        makeqr()
    elif change == "2":
        decodeqr()
    else:
        print("No, only 1 or 2")
        start()

print("Hi, i can make QR code with your text or decode your QR code.")
start()