import qrcode
import os

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    while True:
        print("\n========== QR Code Generator ==========")
        print("1. Text")
        print("2. Phone Number")
        print("3. Website")
        print("4. Email")
        print("5. Image URL/Path")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            data = input("Enter text: ")

        elif choice == "2":
            phone = input("Enter phone number: ")
            data = f"tel:{phone}"

        elif choice == "3":
            data = input("Enter website URL: ")

        elif choice == "4":
            email = input("Enter email: ")
            data = f"mailto:{email}"

        elif choice == "5":
            image = input("Enter image URL or image path: ")

            if os.path.exists(image):
                print("\nNote: QR codes cannot store images directly.")
                print("It will only store the file path.")
            data = image

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            continue

        filename = input("Output file name: ") + ".png"
        generate_qr(data, filename)
        print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    main()


