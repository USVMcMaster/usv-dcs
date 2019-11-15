from flask import Blueprint, jsonify, request, make_response
import urllib.request
import numpy as np
import cv2


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
        image = process_image(static_map_url) #<-- opencv processed image (mask)
        retval, encoded_image = cv2.imencode('.png', image)
        response = make_response(encoded_image.tobytes())
        response.headers['Content-Type'] = 'image/png'
        return response
    
    return 'You can\'t see this if you give the right url, some background stuff will happen!'

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def process_image(url):
    image = url_to_image(url)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lower_blue = np.asarray([165,216,237])
    upper_blue = np.asarray([175,222,255])

    mask = cv2.inRange(rgb_image, lower_blue, upper_blue)

    return mask

# Copy this link and send as ?map= for some magic
# https%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fcenter%3D43.266951%2C-79.921734%26zoom%3D15%26size%3D480x480%26markers%3D%26style%3Dfeature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff%26style%3Dfeature%3Aroad%7Cvisibility%3Aoff%26key%3DAIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs
