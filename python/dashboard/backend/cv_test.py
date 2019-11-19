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

    return mask, res

def image_to_mesh(image):

    mesh = mb.build_mesh(image, 5)

    pkl = pickle.dumps(mesh, protocol=pickle.HIGHEST_PROTOCOL)

    mesh_image = zeros_like(image)

    for x1, x2, y1, y2 in mesh['boxes']:
        mesh_image[x1:x2, y1:y2] = random.randint(64, 255)

    return pkl, mesh_image

image, res = mask_image()

if len(image.shape) > 2:
    image = image[:, :, 0]

pkl, mesh_image = image_to_mesh(image)

true_src = (632, 6)
true_dst = (197, 286)

path_src = tuple(list(true_src)[::-1])
path_dst = tuple(list(true_dst)[::-1])

path, visited_boxes = pf.find_path(path_src, path_dst, pickle.loads(pkl))

for pt_pair in path:
    formatted_pt_pair = [list(data) for data in pt_pair]
    formatted_pt_pair[0] = formatted_pt_pair[0][::-1]
    formatted_pt_pair[1] = formatted_pt_pair[1][::-1]

    cv2.line(res, tuple(formatted_pt_pair[0]), tuple(formatted_pt_pair[1]), (127,132,241), 5)
    # for pt in pt_pair:
    #     pt = pt[::-1] <-- true points list (check order to confirm)
    #     res = cv2.circle(res, pt, 1, [123,241,122],5)

cv2.circle(res, true_src,2,(0,255,0),2,8,0)
cv2.circle(res, true_dst,2,(0,0,255),2,8,0)

cv2.imshow("path", res)
cv2.waitKey(0)