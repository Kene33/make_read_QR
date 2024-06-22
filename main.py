import qrcode
import cv2
from pyzbar import pyzbar


def make_qr():
    link = str(input("Write link or any text for make QR Code > "))
    img = qrcode.make(link)
    img.save("your_code.png")

    print("Done! I save your QR Code in your_code.png")

def decode_qr():
    while True:
        try:
            qrlink = str(input("Enter the path to the QR Code image > "))
            img = cv2.imread(qrlink)
            barcodes = pyzbar.decode(img)

            for barcode in barcodes:
                qrdata = barcode.data.decode("utf-8")
                print(f"Result: {qrdata}")
        except:
            print("Error! Maybe incorrect path to image.")
            break
    
        quas = str(input("Do you want to decode more QR codes? (Yes/No) > "))

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
