from PIL import Image
import numpy as np
from tkinter import Tk, filedialog, simpledialog, messagebox
import os

# Function to encrypt the image
def encrypt_image(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)
    encrypted_pixels = np.zeros_like(pixels)

    # Swap RGB channels
    encrypted_pixels[:, :, 0] = pixels[:, :, 1]
    encrypted_pixels[:, :, 1] = pixels[:, :, 2]
    encrypted_pixels[:, :, 2] = pixels[:, :, 0]

    encrypted_image = Image.fromarray(encrypted_pixels)

    # Save encrypted image
    encrypted_path = os.path.join(os.path.dirname(image_path), "encrypted_image.jpg")
    encrypted_image.save(encrypted_path)
    print(f"✅ Encrypted image saved to: {encrypted_path}")
    messagebox.showinfo("Success", f"Encrypted image saved to:\n{encrypted_path}")
    return encrypted_path

# Function to decrypt the image
def decrypt_image(encrypted_image_path):
    img = Image.open(encrypted_image_path).convert("RGB")
    pixels = np.array(img)
    decrypted_pixels = np.zeros_like(pixels)

    # Reverse the RGB swap
    decrypted_pixels[:, :, 0] = pixels[:, :, 2]
    decrypted_pixels[:, :, 1] = pixels[:, :, 0]
    decrypted_pixels[:, :, 2] = pixels[:, :, 1]

    decrypted_image = Image.fromarray(decrypted_pixels)

    # Save decrypted image
    decrypted_path = os.path.join(os.path.dirname(encrypted_image_path), "decrypted_image.jpg")
    decrypted_image.save(decrypted_path)
    print(f"✅ Decrypted image saved to: {decrypted_path}")
    messagebox.showinfo("Success", f"Decrypted image saved to:\n{decrypted_path}")
    return decrypted_path

# GUI to select image
def select_image():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    return file_path

# GUI to ask Encrypt or Decrypt
def ask_action():
    Tk().withdraw()
    action = simpledialog.askstring(
        "Choose Action", "Type 'encrypt' to encrypt or 'decrypt' to decrypt:"
    )
    return action.lower().strip() if action else None

# Main program
if __name__ == "__main__":
    action = ask_action()
    if action not in ["encrypt", "decrypt"]:
        print("❌ Invalid action or cancelled. Exiting.")
        exit()

    print("📂 Please select an image file...")
    image_path = select_image()
    if not image_path:
        print("❌ No file selected. Exiting.")
        exit()

    if action == "encrypt":
        encrypt_image(image_path)
    elif action == "decrypt":
        decrypt_image(image_path)
