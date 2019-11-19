import numpy as np
import cv2

import astar.meshbuilder as mb
import astar.pathfinder as pf
from numpy import zeros_like
import pickle
import random

def mask_image():
    image = cv2.imread('image.png', cv2.IMREAD_COLOR)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lower_blue = np.asarray([165,216,237])
    upper_blue = np.asarray([175,222,255])

    mask = cv2.inRange(rgb_image, lower_blue, upper_blue)
    res = cv2.bitwise_and(image,image,mask = mask)

    # # mask = cv2.resize(mask,(100,100))

    return image, mask, res

def image_to_mesh(image):

    mesh = mb.build_mesh(image, 5)

    pkl = pickle.dumps(mesh, protocol=pickle.HIGHEST_PROTOCOL)

    mesh_image = zeros_like(image)

    for x1, x2, y1, y2 in mesh['boxes']:
        mesh_image[x1:x2, y1:y2] = random.randint(64, 255)

    return pkl, mesh_image

image, mask, res = mask_image()

if len(mask.shape) > 2:
    mask = mask[:, :, 0]

pkl, mesh_image = image_to_mesh(mask)

true_src = (632, 6)
true_dst = (197, 286)

path_src = tuple(list(true_src)[::-1])
path_dst = tuple(list(true_dst)[::-1])

path, visited_boxes = pf.find_path(path_src, path_dst, pickle.loads(pkl))

for pt_pair in path:
    formatted_pt_pair = [list(data) for data in pt_pair]
    formatted_pt_pair[0] = formatted_pt_pair[0][::-1]
    formatted_pt_pair[1] = formatted_pt_pair[1][::-1]

    cv2.line(image, tuple(formatted_pt_pair[0]), tuple(formatted_pt_pair[1]), (90,139,255), 5)
    for pt in pt_pair:
        pt = pt[::-1] # <-- true points list (check order to confirm)
        image = cv2.circle(image, pt, 2, (255,145,147),2,8,0)

cv2.circle(image, true_src,2,(0,255,0),2,8,0)
cv2.circle(image, true_dst,2,(0,0,255),2,8,0)

cv2.imshow("path", image)
cv2.waitKey(0)