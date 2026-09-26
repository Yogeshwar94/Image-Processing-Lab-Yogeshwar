import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread('neg.png')

#Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)
plt.title('Sharpening')
plt.imshow('sharpened_image')
plt.show()