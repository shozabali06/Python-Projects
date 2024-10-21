import tkinter as tk
from tkinter import filedialog
import qrcode

def generate_qr():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    img.save(save_path)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create the input field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create the generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
