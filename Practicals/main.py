# import cv2
# img = cv2.imread("tomato.png", cv2.IMREAD_COLOR)
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread("tomato.png")
# plt.imshow(img)
# plt.waitforbuttonpress()
# plt.close()

#import cv2, numpy and matplotlib libraries

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread("tomato.png")
# # Converting BGR color to RGB color format
# RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #Displaying image using plt.imshow() method
# plt.imshow(RGB_img)
# # hold the window
# plt.waitforbuttonpress()
# plt.close("all")

# Python program to explain cv2.imread() method 
# import cv2
# path = r'tomato.png'
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#


# importing cv2
# import cv2
# image_path = r'C:\Users\yogesh kadam\Desktop\tomato.png'
# directory = r'C:\Users\yogesh kadam\Desktop'
# # importing os module  
# import os
# image_path = r'tomato.png'
# directory = r'C:\Users\yogesh kadam\Desktop'
# img = cv2.imread(image_path)
# os.chdir(directory)
# print("Before saving image")
# print(os.listdir(directory))
# filename ="savedImage.jpg"
# cv2.imwrite(filename, img)
# print("After saving image")
# print(os.listdir(directory))
# print("Successfully saved")

import cv2
import numpy as np
image1 = cv2.imread("sky.jpg")
image2 = cv2.imread("nature.png")
weightedSum = cv2.addWeighted(sky,0.5, nature, 0.4, 0)
cv2.imshow("Weighted Image", weightedSum)
if cv2.waitKey(0) &amp; 0xff == 27:
cv2.destroyAllWindows()