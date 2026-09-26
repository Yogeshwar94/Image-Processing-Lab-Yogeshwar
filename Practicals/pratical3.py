# import numpy as np
# import cv2 as cv
# img = cv.imread('girl.jpeg', 0)
# rows, cols = img.shape
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv.warpAffine(img, M, (cols, rows))
# cv.imshow('yogeshwar CS25D026', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# img = cv.imread('girl.jpeg',0)
# rows, cols = img.shape
# M = np.float32([[1, 0, 0],
# [0, -1, rows],
# [0, 0, 1]])
# reflected_img = cv.warpPerspective(img, M,
# (int(cols),
# int(rows)))
# cv.imshow('CS25D026', reflected_img)
# cv.imwrite('reflection_out.jpeg', reflected_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# img = cv.imread('girl.jpeg', 0)
# rows, cols = img.shape
# M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
# img_rotation = cv.warpAffine(img,
# cv.getRotationMatrix2D((cols/2, rows/2),
# 30, 0.6),
# (cols, rows))
# cv.imshow('CS25D026', img_rotation)
# cv.imwrite('rotation_out.jpeg', img_rotation)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv

# Read image
img = cv.imread("girl.jpeg", 0)

# Check image
if img is None:
    print("Error: girl.jpeg not found!")
    exit()

rows, cols = img.shape

# Shrink image
img_shrinked = cv.resize(img, (250, 200), interpolation=cv.INTER_AREA)

# Enlarge image
img_enlarged = cv.resize(img_shrinked, None,
                         fx=1.5,
                         fy=1.5,
                         interpolation=cv.INTER_CUBIC)

# Show images
cv.imshow("Original", img)
cv.imshow("Shrinked", img_shrinked)
cv.imshow("Enlarged", img_enlarged)

cv.waitKey(0)
cv.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# img = cv.imread('girl.jpeg', 0)
# cropped_img = img[100:300, 100:300]
# cv.imwrite('cropped_out.jpeg', cropped_img)
# cv.waitKey(0)
# cv.destroyAllWindows()