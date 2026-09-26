import cv2
import os

# ---------- Function to calculate compression ratio ----------
def compression_ratio(original_file, compressed_file):
    """
    Compression Ratio = Original Size / Compressed Size
    """
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)

    original_kb = original_size / 1024
    compressed_kb = compressed_size / 1024

    ratio = original_size / compressed_size

    return ratio, original_kb, compressed_kb


# ---------- Load the image ----------
image_path = "img.jpeg"   # Put your actual image name here

image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(
        "Image not found. Check the image path and filename."
    )


# ---------- Lossy Compression (JPEG) ----------
jpeg_quality = 30

lossy_output = "compressed_lossy.jpg"

cv2.imwrite(
    lossy_output,
    image,
    [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality]
)


# ---------- Lossless Compression (PNG) ----------
png_compression = 9

lossless_output = "compressed_lossless.png"

cv2.imwrite(
    lossless_output,
    image,
    [cv2.IMWRITE_PNG_COMPRESSION, png_compression]
)


# ---------- Calculate Compression Ratios ----------
lossy_ratio, original_kb, lossy_kb = compression_ratio(
    image_path,
    lossy_output
)

lossless_ratio, _, lossless_kb = compression_ratio(
    image_path,
    lossless_output
)


# ---------- Print Results ----------
print(f"Original Size: {original_kb:.2f} KB")

print(
    f"Lossy JPEG Size: {lossy_kb:.2f} KB "
    f"(Quality={jpeg_quality})"
)

print(
    f"Lossless PNG Size: {lossless_kb:.2f} KB "
    f"(Compression={png_compression})"
)

print(f"Lossy Compression Ratio: {lossy_ratio:.2f}:1")

print(f"Lossless Compression Ratio: {lossless_ratio:.2f}:1")


# ---------- Display Images ----------
cv2.imshow("Original", image)

cv2.imshow(
    "Lossy JPEG",
    cv2.imread(lossy_output)
)

cv2.imshow(
    "Lossless PNG",
    cv2.imread(lossless_output)
)

cv2.waitKey(0)
cv2.destroyAllWindows()