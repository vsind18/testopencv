import cv2
import numpy as np
path = r"E:\training_xu_ly_anh_irobotlab\de_test_pencv\de_test_pencv\anh1.png"
img = cv2.imread(path,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyWindow()
