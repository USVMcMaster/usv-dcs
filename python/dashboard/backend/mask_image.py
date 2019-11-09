import numpy as np
import urllib.request
import cv2


# hsv for google's water
# 206,33,100
# #AADAFF
#ADDCED
url="https://maps.googleapis.com/maps/api/staticmap?center=43.266951,-79.921734&zoom=15&size=480x480&markers=&style=feature:all|element:labels|visibility:off&style=feature:road|visibility:off&key=AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs"

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

 
    # return the image
    return image

image = url_to_image(url)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
lower_blue = np.asarray([165,216,237])
upper_blue = np.asarray([175,222,255])
# upper_blue = np.asarray([170,218,255])

mask = cv2.inRange(rgb_image, lower_blue, upper_blue)
inverted_mask = cv2.bitwise_and(image, image, mask=mask)

cv2.namedWindow('default_map', flags=cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('masked_map', flags=cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('inverted_mask_map', flags=cv2.WINDOW_GUI_NORMAL)

cv2.imshow("default_map", image)
cv2.imshow("masked_map", mask)
cv2.imshow("inverted_mask_map", inverted_mask)
cv2.waitKey(0)