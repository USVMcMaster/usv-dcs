import astar.meshbuilder as mb
import astar.pathfinder as pf
import urllib.request
import numpy as np
import pickle
import random
import cv2


def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def mask_image(url, debug_mode = False):

    image = url_to_image(url) if not debug_mode else cv2.imread('image.png', cv2.IMREAD_COLOR)

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lower_blue = np.asarray([165,216,237])
    upper_blue = np.asarray([175,222,255])

    mask = cv2.inRange(rgb_image, lower_blue, upper_blue)

    return image, mask

def image_to_mesh(image):

    mesh = mb.build_mesh(image, 5)

    pkl = pickle.dumps(mesh, protocol=pickle.HIGHEST_PROTOCOL)

    mesh_image = np.zeros_like(image)

    for x1, x2, y1, y2 in mesh['boxes']:
        mesh_image[x1:x2, y1:y2] = random.randint(64, 255)

    return pkl, mesh_image

def gen_path(path_src, path_dst, pkl):
    path, visited_boxes = pf.find_path(path_src, path_dst, pickle.loads(pkl))

    return path, visited_boxes

def path_cleanup(path):
        
    clean_path = []

    path.reverse()

    for pt_pair in path:

        formatted_pt_pair = [list(data) for data in pt_pair]
        formatted_pt_pair[0] = formatted_pt_pair[0][::-1]
        formatted_pt_pair[1] = formatted_pt_pair[1][::-1]

        clean_path.append([formatted_pt_pair[1], formatted_pt_pair[0]])

    return clean_path

def get_points(path):
    raw_points = []
    for path_pair in path:
        for point in path_pair:
            raw_points.append(point)

    points = []
    # Removing duplicate points and appending to list points
    [points.append(point) for point in raw_points if point not in points]

    return points

if __name__ == "__main__":
    
    url = 'image.png'
    image, mask = mask_image(url, debug_mode=True)

    if len(mask.shape) > 2:
        mask = mask[:, :, 0]

    pkl, mesh_image = image_to_mesh(mask)

    true_src = (632, 6)
    true_dst = (197, 286)

    path_src = tuple(list(true_src)[::-1])
    path_dst = tuple(list(true_dst)[::-1])
    
    path, visited_boxes = gen_path(path_src, path_dst, pkl)

    # list of paths -> path pairs -> points
    path = path_cleanup(path)
    points = get_points(path)

    # Show route
    for pt_pair in path:
        cv2.line(image, tuple(pt_pair[0]), tuple(pt_pair[1]), (90,139,255), 1)

    # Show points
    for point in points:
        cv2.circle(image, tuple(point), 2, (255,145,147),1,8,0)

    cv2.circle(image, true_src,2,(0,255,0),2,8,0)
    cv2.circle(image, true_dst,2,(0,0,255),2,8,0)

    cv2.imshow("path", mask)
    cv2.waitKey(0)