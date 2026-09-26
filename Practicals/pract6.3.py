
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# --------------------------------
# Step 1: Select the noisy image
# --------------------------------

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Noisy Image",
    filetypes=[
        ("Image files", "*.png *.jpg *.jpeg *.bmp"),
        ("All files", "*.*")
    ]
)

# Check if user selected an image
if not image_path:
    print("ERROR: No image selected.")
    exit()

print("Selected image:")
print(image_path)


# --------------------------------
# Step 2: Read the noisy image
# --------------------------------

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("ERROR: OpenCV could not read the selected image.")
    exit()

print("Image loaded successfully.")


# --------------------------------
# Step 3: Apply Gaussian Blur
# --------------------------------

restored = cv2.GaussianBlur(img, (5, 5), 0)


# --------------------------------
# Step 4: Display results
# --------------------------------

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Gaussian Noisy Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(restored, cmap="gray")
plt.title("Restored (Gaussian Blur)")
plt.axis("off")

plt.tight_layout()
plt.show()

