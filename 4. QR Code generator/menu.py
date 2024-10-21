import qrcode
import os


def showMenu():
    print(
        "Welcome to QR Code Generator 😺\n\nChoose option from menu:\n\n1. Single\n2. Batch\n0. Exit\n"
    )


def getInput():
    while True:
        try:
            opt = int(input())
            if opt == 1 or opt == 2 or opt == 0:
                return opt
            else:
                print("\nInvalid integer.")
        except:
            print("\ninvalid Input. 😶")


def ensure_directory():
    if not os.path.exists("QR Codes"):
        os.makedirs("QR Codes")


while True:
    showMenu()
    opt = getInput()
    if opt == 1:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        data = input("\nEnter data: ")
        fileName = input("\n Name the file: ")
        while True:  # Validate file type
            fileType = input("Save as (png, jpg): ").lower()
            if fileType in ["png", "jpg"]:
                break
            print("Invalid file type. Please enter 'png' or 'jpg'.")
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        ensure_directory()

        img.save(f"QR Codes/{fileName}.{fileType}")

        print("\nQR Code saved.\n")
    elif opt == 2:

        def get_user_input():
            # Get user input as a comma-separated string
            user_input = input("Enter data for QR codes (separated by commas): ")
            # Split the input by commas and create a list
            return [data.strip() for data in user_input.split(",")]

        data_list = get_user_input()
        fileType = input("Save as (png, jpg): ")

        for i, data in enumerate(data_list):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            ensure_directory()
            img.save(f"QR Codes/qrcode_{i}.{fileType}")

        print("\nSaved ✅\n")

    else:
        exit()
