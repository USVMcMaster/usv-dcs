from flask import Blueprint, jsonify, request, make_response
import urllib.request
import numpy as np
import cv2

# from matplotlib.pyplot import imread, imsave
import astar.meshbuilder as mb
import astar.pathfinder as pf
from numpy import zeros_like
import pickle
import random

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return "Welcome to the landing page of the USV Capstone Project!"

@main.route('/test_data')
def test_data():
    return jsonify(['a','b'])

@main.route('/mask', methods=['GET'])
def gen_mask():
    static_map_url = request.args.get('map')

    if static_map_url:
        # image = url_to_image(static_map_url) <-- input image
        image = mask_image(static_map_url) #<-- opencv processed image (mask)

        # if len(image.shape) > 2:
        #     image = image[:, :, 0]       

        pkl, mesh_image = image_to_mesh(image)
        
        src = (6,632)
        # src = (632, 6)
        
        dst = (286,197)
        # dst = (197,286)
        path, visited_boxes = pf.find_path(src, dst, pickle.loads(pkl))

        print('\n\npath:', path, '\n\n')
        # print(path[::-1])
        for pt_pair in path:
            cv2.line(image, pt_pair[0], pt_pair[1], (127,0,0), 5)
            # for pt in pt_pair:
                # image = cv2.circle(image, pt, 1, [255,0,0],-1)
        cv2.circle(image, (0,0),30,(255,0,0),2,8,0)
        retval, encoded_image = cv2.imencode('.png', image)
        response = make_response(encoded_image.tobytes())
        response.headers['Content-Type'] = 'image/png'
        return response
    
    return 'You can\'t see this if you give the right url, but some background stuff will happen!'

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def mask_image(url):
    image = url_to_image(url)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lower_blue = np.asarray([165,216,237])
    upper_blue = np.asarray([175,222,255])

    mask = cv2.inRange(rgb_image, lower_blue, upper_blue)
    # mask = cv2.resize(mask,(100,100))

    return mask

def image_to_mesh(image):
    

    mesh = mb.build_mesh(image, 5)

    pkl = pickle.dumps(mesh, protocol=pickle.HIGHEST_PROTOCOL)

    mesh_image = zeros_like(image)

    for x1, x2, y1, y2 in mesh['boxes']:
        mesh_image[x1:x2, y1:y2] = random.randint(64, 255)

    return pkl, mesh_image

    # with open('map' + '.mesh.pickle', 'wb') as f:
    #     pickle.dump(mesh, f, protocol=pickle.HIGHEST_PROTOCOL)

    # atlas = zeros_like(image)
    # for x1, x2, y1, y2 in mesh['boxes']:
    #     atlas[x1:x2, y1:y2] = random.randint(64, 255)

    # imsave('map' + '.mesh.png', atlas)

    # return pkl, mesh_image



# Copy this link and send as ?map= for some magic
# https%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fcenter%3D43.266951%2C-79.921734%26zoom%3D15%26size%3D640x640%26markers%3D%26style%3Dfeature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff%26style%3Dfeature%3Aroad%7Cvisibility%3Aoff%26key%3DAIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs








# expected data
'''
src, dst:  (6, 632) (286, 197)
source (161, 256)
source (167, 246)
source (172, 227)
source (178, 219)
source (181, 219)
source (182, 217)
source (184, 217)
source (188, 213)
source (191, 213)
source (202, 208)
source (213, 208)
source (219, 208)
source (222, 208)
source (223, 206)
source (229, 206)
source (238, 202)
source (246, 201)
source (253, 200)
source (273, 198)
source (282, 197)
opposite goal (157, 267)
opposite goal (157, 269)
opposite goal (157, 273)
opposite goal (157, 276)
opposite goal (155, 282)
opposite goal (155, 285)
opposite goal (152, 290)
opposite goal (146, 293)
opposite goal (142, 302)
opposite goal (138, 308)
opposite goal (136, 312)
opposite goal (135, 314)
opposite goal (133, 315)
opposite goal (133, 317)
opposite goal (133, 321)
opposite goal (133, 332)
opposite goal (128, 341)
opposite goal (126, 341)
opposite goal (125, 341)
opposite goal (122, 342)
opposite goal (113, 362)
opposite goal (113, 368)
opposite goal (102, 383)
opposite goal (81, 413)
opposite goal (52, 442)
opposite goal (41, 481)
opposite goal (21, 502)
opposite goal (21, 513)
opposite goal (11, 561)
opposite goal (11, 601)
opposite goal (11, 621)
[((157, 267), (161, 256)), ((161, 256), (167, 246)), ((167, 246), (172, 227)), ((172, 227), (178, 219)), ((178, 219), (181, 219)), ((181, 219), (182, 217)), ((182, 217), (184, 217)), ((184, 217), (188, 213)), ((188, 213), (191, 213)), ((191, 213), (202, 208)), ((202, 208), (213, 208)), ((213, 208), (219, 208)), ((219, 208), (222, 208)), ((222, 208), (223, 206)), ((223, 206), (229, 206)), ((229, 206), (238, 202)), ((238, 202), (246, 201)), ((246, 201), (253, 200)), ((253, 200), (273, 198)), ((273, 198), (282, 197)), ((282, 197), (286, 197)), ((157, 267), (157, 269)), ((157, 269), (157, 273)), ((157, 273), (157, 276)), ((157, 276), (155, 282)), ((155, 282), (155, 285)), ((155, 285), (152, 290)), ((152, 290), (146, 293)), ((146, 293), (142, 302)), ((142, 302), (138, 308)), ((138, 308), (136, 312)), ((136, 312), (135, 314)), ((135, 314), (133, 315)), ((133, 315), (133, 317)), ((133, 317), (133, 321)), ((133, 321), (133, 332)), ((133, 332), (128, 341)), ((128, 341), (126, 341)), ((126, 341), (125, 341)), ((125, 341), (122, 342)), ((122, 342), (113, 362)), ((113, 362), (113, 368)), ((113, 368), (102, 383)), ((102, 383), (81, 413)), ((81, 413), (52, 442)), ((52, 442), (41, 481)), ((41, 481), (21, 502)), ((21, 502), (21, 513)), ((21, 513), (11, 561)), ((11, 561), (11, 601)), ((11, 601), (11, 621)), ((11, 621), (6, 632))]
'''
