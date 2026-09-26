
import cv2
import numpy as np
import os

# -------------------------------------------------
# PART 1: Generate mask & restore using TELEA
# -------------------------------------------------

# Use the FULL path to your damaged image
damaged_path = r"C:\Users\yogesh kadam\Desktop\PythonProject\cat_damaged.png"

# Step 1: Read the damaged image
damaged_img = cv2.imread(damaged_path)

# Check whether image was loaded successfully
if damaged_img is None:
    print("ERROR: Could not read the image.")
    print("Check that this file exists:")
    print(damaged_path)
    exit()

print("Damaged image loaded successfully.")

# Step 2: Get image dimensions
height, width = damaged_img.shape[:2]

# Create a black mask
mask = np.zeros((height, width), dtype=np.uint8)

# Generate mask
for i in range(height):
    for j in range(width):

        # If pixel is black, mark it as damaged
        if damaged_img[i, j].sum() == 0:
            mask[i, j] = 255
        else:
            mask[i, j] = 0

# Save generated mask
cv2.imwrite("generated_mask.png", mask)

# Step 3: Perform inpainting using TELEA
restored_telea = cv2.inpaint(
    damaged_img,
    mask,
    3,
    cv2.INPAINT_TELEA
)

# Save TELEA result
cv2.imwrite("restored_telea.png", restored_telea)


# -------------------------------------------------
# PART 2: Restore using predefined mask
# -------------------------------------------------

# Step 4: Read predefined mask
mask_predefined = cv2.imread(
    r"C:\Users\yogesh kadam\Desktop\PythonProject\cat_mask.png",
    cv2.IMREAD_GRAYSCALE
)

# Check whether predefined mask was loaded
if mask_predefined is None:
    print("ERROR: Could not read cat_mask.png")
    exit()

# Make sure mask and image have the same size
if mask_predefined.shape != (height, width):
    mask_predefined = cv2.resize(
        mask_predefined,
        (width, height)
    )

# Step 5: Inpaint using Navier-Stokes method
restored_ns = cv2.inpaint(
    damaged_img,
    mask_predefined,
    3,
    cv2.INPAINT_NS
)

# Save Navier-Stokes result
cv2.imwrite("restored_ns.png", restored_ns)


# -------------------------------------------------
# PART 3: Display results
# -------------------------------------------------

cv2.imshow("Original Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask)
cv2.imshow("Restored - TELEA", restored_telea)
cv2.imshow("Predefined Mask", mask_predefined)
cv2.imshow("Restored - Navier-Stokes", restored_ns)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Processing completed successfully.")
print("Generated files:")
print("  generated_mask.png")
print("  restored_telea.png")
print("  restored_ns.png")

