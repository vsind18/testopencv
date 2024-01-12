import cv2
import numpy as np
from matplotlib import pyplot as plt
path = r'E:\training_xu_ly_anh_irobotlab\de_test_pencv\de_test_pencv\anh2.PNG'
img = cv2.imread(path, 0)
kernel = np.ones((27,27), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
kernel1 = np.ones((23,23), np.uint8)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)
titles = ["Original image","Output 1", "Output 2"]
images = [img, opening, closing]
for i in range(3):
    plt.subplot(3, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()