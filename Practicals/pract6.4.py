
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# --------------------------------
# Step 1: Select the noisy image
# --------------------------------

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Salt and Pepper Noisy Image",
    filetypes=[
        ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
        ("All Files", "*.*")
    ]
)

if not image_path:
    print("ERROR: No image selected.")
    exit()

print("Selected file:")
print(image_path)


# --------------------------------
# Step 2: Read the noisy image
# --------------------------------

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("ERROR: OpenCV could not read this image.")
    exit()

print("Image loaded successfully!")


# --------------------------------
# Step 3: Apply Median Filter
# --------------------------------

restored = cv2.medianBlur(img, 5)


# --------------------------------
# Step 4: Display results
# --------------------------------

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Salt & Pepper Noise")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(restored, cmap="gray")
plt.title("Restored (Median Filter)")
plt.axis("off")

plt.tight_layout()
plt.show()

