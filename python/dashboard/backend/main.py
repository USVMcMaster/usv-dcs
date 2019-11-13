from flask import Flask, request, make_response
import urllib.request
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def gen_route():
    key = 'map'
    static_map_url = request.args.get(key)
    if static_map_url:
        # image = url_to_image(static_map_url) <-- input image
        image = process_image(static_map_url) #<-- opencv processed image (mask)
        retval, encoded_image = cv2.imencode('.png', image)
        response = make_response(encoded_image.tobytes())
        response.headers['Content-Type'] = 'image/png'
        return response
    
    return f'Welcome to the backend of the USV project. There is nothing to see here.\n'


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

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)