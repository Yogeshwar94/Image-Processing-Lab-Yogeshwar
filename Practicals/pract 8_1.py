import cv2
import numpy as np

# ---------- Load the image ----------
image_path = r"C:\Users\yogesh kadam\Desktop\PythonProject\ybk.jpg"

# Replace image.jpg with your actual image filename
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image not found. Check the path.")

# ---------- Threshold to ensure binary ----------
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# ---------- Define structuring element ----------
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# ---------- Erosion ----------
erosion = cv2.erode(binary, kernel, iterations=1)

# ---------- Dilation ----------
dilation = cv2.dilate(binary, kernel, iterations=1)

# ---------- Opening (Erosion followed by Dilation) ----------
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# ---------- Closing (Dilation followed by Erosion) ----------
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# ---------- Display Results ----------
cv2.imshow("Original Binary", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()