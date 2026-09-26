
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# --------------------------------
# Step 1: Read the damaged image
# --------------------------------

damaged_path = r"C:\Users\yogesh kadam\Desktop\PythonProject\cat_damaged.png"
mask_path = r"C:\Users\yogesh kadam\Desktop\PythonProject\cat_mask.png"

damaged_img = cv2.imread(damaged_path)

# Check if image was loaded
if damaged_img is None:
    print("ERROR: cat_damaged.png could not be found or opened.")
    print("Check this path:")
    print(damaged_path)
    exit()

print("Damaged image loaded successfully.")


# --------------------------------
# Step 2: Create mask automatically
# --------------------------------

height, width = damaged_img.shape[:2]

# Create a single-channel grayscale mask
mask_auto = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):

        # Non-black pixel
        if damaged_img[i, j].sum() > 0:
            mask_auto[i, j] = 0

        # Black pixel = damaged area
        else:
            mask_auto[i, j] = 255


# Save generated mask
cv2.imwrite("generated_mask.png", mask_auto)


# --------------------------------
# Step 3: Restore with TELEA method
# --------------------------------

restored_telea = cv2.inpaint(
    damaged_img,
    mask_auto,
    3,
    cv2.INPAINT_TELEA
)

cv2.imwrite("restored_telea.png", restored_telea)


# --------------------------------
# Step 4: Restore using predefined
# mask with Navier-Stokes method
# --------------------------------

mask_predefined = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Check if predefined mask was loaded
if mask_predefined is None:
    print("ERROR: cat_mask.png could not be found or opened.")
    print("Check this path:")
    print(mask_path)
    exit()

# Make sure mask has same size as damaged image
if mask_predefined.shape != (height, width):
    mask_predefined = cv2.resize(
        mask_predefined,
        (width, height)
    )

restored_ns = cv2.inpaint(
    damaged_img,
    mask_predefined,
    3,
    cv2.INPAINT_NS
)

cv2.imwrite("restored_ns.png", restored_ns)


# --------------------------------
# Step 5: Plot results using Matplotlib
# --------------------------------

images = [
    damaged_img,
    mask_auto,
    restored_telea,
    restored_ns
]

titles = [
    "Original Damaged",
    "Generated Mask",
    "Restored (Telea)",
    "Restored (Navier-Stokes)"
]

plt.figure(figsize=(12, 6))

for i in range(4):

    plt.subplot(2, 2, i + 1)

    # Display grayscale mask
    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap="gray")

    # Display color image
    else:
        plt.imshow(
            cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
        )

    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()

print("Processing completed successfully!")
print("Generated files:")
print("generated_mask.png")
print("restored_telea.png")
print("restored_ns.png")

