import numpy as np
from PIL import Image
import os

# Q4(a): Convert Image to NumPy Array

def img_to_array(path):
    img = Image.open(path)

    # RGB Image
    if img.mode == "RGB":
        array = np.array(img)

        # Save RGB array
        np.savetxt("rgb_image.txt",
                   array.reshape(-1, 3),
                   fmt="%d")

        print("RGB Image Converted Successfully!")
        print("Original Shape:", array.shape)
        print("Saved as rgb_image.txt")

    # Grayscale Image
    elif img.mode == "L":
        array = np.array(img)

        # Save Grayscale array
        np.savetxt("grayscale_image.txt",
                   array,
                   fmt="%d")

        print("Grayscale Image Converted Successfully!")
        print("Original Shape:", array.shape)
        print("Saved as grayscale_image.txt")

    else:
        print("Unsupported Image Mode:", img.mode)

# Create sample images for testing

rgb = Image.new("RGB", (5, 5), color=(255, 0, 0))
rgb.save("sample_rgb.png")

gray = Image.new("L", (5, 5), color=128)
gray.save("sample_gray.png")

# Convert images
img_to_array("sample_rgb.png")
img_to_array("sample_gray.png")


# Q4(b): Load Saved Files

print("\nLoading RGB Image Array:")
rgb_loaded = np.loadtxt("rgb_image.txt", dtype=int)
print(rgb_loaded)

print("\nLoading Grayscale Image Array:")
gray_loaded = np.loadtxt("grayscale_image.txt", dtype=int)
print(gray_loaded)
