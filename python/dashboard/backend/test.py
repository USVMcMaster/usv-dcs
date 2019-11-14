import cv2
import numpy as np
import pdb


image = cv2.imread('sample_map.png')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
lower_blue = np.asarray([165,216,237])
upper_blue = np.asarray([175,222,255])

mask = cv2.inRange(rgb_image, lower_blue, upper_blue)
cv2.imshow("masked_map", mask)
cv2.waitKey(0)

start = [220, 220]
end = [480, 10]