import cv2
import numpy as np
path = r"E:\training_xu_ly_anh_irobotlab\de_test_pencv\de_test_pencv\anh3.png"
img = cv2.imread(path, 1)
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([255, 100, 100])
blue_mask = cv2.inRange(img, lower_blue, upper_blue)
blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#bôi xanh lá
cv2.drawContours(img, blue_contours, -1, (0, 255, 0), 17)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
