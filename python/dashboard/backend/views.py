from flask import Blueprint, jsonify, request, make_response, send_file
import base64
import cv_processing as cvp
import json

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return "Welcome to the landing page of the USV Capstone Project!"

@main.route('/mask', methods=['GET'])
def gen_mask():
    static_map_url = request.args.get('map')

    if static_map_url:

        image, mask = cvp.mask_image(static_map_url) #<-- opencv processed image (mask)

        if len(mask.shape) > 2:
            mask = mask[:, :, 0]

        pkl, mesh_image = cvp.image_to_mesh(mask)

        true_src = (632, 6)
        true_dst = (197, 286)

        path_src = tuple(list(true_src)[::-1])
        path_dst = tuple(list(true_dst)[::-1])

        path, visited_boxes = cvp.gen_path(path_src, path_dst, pkl)

        # list of paths -> path pairs -> points
        path = cvp.path_cleanup(path)
        points = cvp.get_points(path)

        # Show route
        for pt_pair in path:
            cvp.cv2.line(image, tuple(pt_pair[0]), tuple(pt_pair[1]), (90,139,255), 1)

        # Show points
        for point in points:
            cvp.cv2.circle(image, tuple(point), 2, (255,145,147),1,8,0)

        cvp.cv2.circle(image, true_src,2,(0,255,0),2,8,0)
        cvp.cv2.circle(image, true_dst,2,(0,0,255),2,8,0)

        # cvp.cv2.imwrite("./processed_images/image.png", image)
        # cvp.cv2.imwrite("./processed_images/mask.png", mask)
        # cvp.cv2.imwrite("./processed_images/mesh.png", mesh_image)

        points = json.dumps(points)
        path = json.dumps(path)
        
        output = jsonify({"id":"points", "data":points}, {"id":"path", "data":path})
        return output
    
    return 'Provide a static map url for path planning'

# Copy this link and send as ?map= for some magic
# /mask?map=https%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fcenter%3D43.266951%2C-79.921734%26zoom%3D15%26size%3D640x640%26markers%3D%26style%3Dfeature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff%26style%3Dfeature%3Aroad%7Cvisibility%3Aoff%26key%3DAIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs
