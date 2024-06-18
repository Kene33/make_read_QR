import segno
import cv2
from pyzbar import pyzbar


def make_qr():
    link = str(input("Write link or any text for make QR Code > "))
    qrcode = segno.make(link, micro=False)
    qrcode.save("qrcode.png", scale=6)

    print("Done! I save your QR Code in qrcode.png")

    open_qr = str(input("Open the QR code or exit? (open/exit) > "))
    if open_qr.lower() == "open":
        qrcode.show()
        print("Bye Bye!")
        break
    elif open_qr.lower() == "exit":
        print("Bye Bye!")
        break
    else:
        print("WRITE ONLY open OR exit :)")
        make_qr()

def decode_qr():
    while True:
        qrlink = str(input("Enter the path to the QR Code image > "))
        img = cv2.imread(qrlink)
        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
            qrdata = barcode.data.decode("utf-8")
            print(f"Result: {qrdata}")
        
        print("Do you want to decode more QR codes? (Yes/No) > ")
        quas = str(input(">> "))
        if quas.lower() == "yes":
            decode_qr()
        else:
            break


def start():
    print("Hi, I can make a QR code with your text or decode your QR code.")
    while True:
        choice = input("What do you want to do? (1 - Make QR Code, 2 - Decode QR code, exit - Quit) > ")
        if choice == "1":
            make_qr()
            break
        elif choice == "2":
            decode_qr()
            break
        elif choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Please enter only '1', '2', or 'exit'")
start()
