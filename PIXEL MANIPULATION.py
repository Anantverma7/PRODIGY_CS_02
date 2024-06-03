from PIL import Image

# Define a constant value for the encryption/decryption process
ENCRYPTION_KEY = 50

def encrypt_image(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Create the pixel map

    # Encrypt the image by modifying pixel values
    for i in range(image.size[0]):  # For every pixel in the width
        for j in range(image.size[1]):  # For every pixel in the height
            r, g, b = pixels[i, j]

            # Modify the pixel values
            r = (r + ENCRYPTION_KEY) % 256
            g = (g + ENCRYPTION_KEY) % 256
            b = (b + ENCRYPTION_KEY) % 256

            # Update the pixel with the new values
            pixels[i, j] = (r, g, b)

    # Save the encrypted image
    image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Create the pixel map

    # Decrypt the image by modifying pixel values
    for i in range(image.size[0]):  # For every pixel in the width
        for j in range(image.size[1]):  # For every pixel in the height
            r, g, b = pixels[i, j]

            # Modify the pixel values
            r = (r - ENCRYPTION_KEY) % 256
            g = (g - ENCRYPTION_KEY) % 256
            b = (b - ENCRYPTION_KEY) % 256

            # Update the pixel with the new values
            pixels[i, j] = (r, g, b)

    # Save the decrypted image
    image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

# Example usage
encrypt_image('input_image.jpg', 'encrypted_image.jpg')
decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg')
