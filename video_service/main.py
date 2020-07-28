import time
from PIL import Image
import numpy as np
from cv2 import cv2
from flask import Flask, request, Response
import qi



app = Flask('video_service')
text = ""
session = None
video_service = None


def connect(ip="192.168.1.123", port="9559", language="English"):
    # type: (str, str, str) -> None
    global session, video_service
    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + port)
        video_service = session.service("ALVideoDevice")

        # Register a Generic Video Module

        fps = 20
        print("Robot connected to VIDEO module.")
    except RuntimeError:
        print("Can't connect to Pepper at ip \""
              + ip + "\" on port " + port + ".\n"
              + "Please check your script arguments. "
              + "Run with -h option for help.")


@app.route('/video', methods=['GET'])
def watch():
    try:
        global video_service
        resolution = 0
        colorSpace = 10
        fps = 20
        videoClient = video_service.subscribe("python_GVM", resolution, colorSpace, fps)
        print 'getting images in remote'

        result = videoClient.getImageRemote(videoClient)

        # create image
        width = result[0]
        height = result[1]
        image = np.zeros((height, width, 3), np.uint8)

        key = 0

        while key != 27:
            # get image
            result = videoClient.getImageRemote(videoClient)

            if result == None:
                print 'cannot capture.'
            elif result[6] == None:
                print 'no image data string.'
            else:

                # translate value to mat
                values = map(ord, list(result[6]))
                i = 0
                for y in range(0, height):
                    for x in range(0, width):
                        image.itemset((y, x, 0), values[i + 0])
                        image.itemset((y, x, 1), values[i + 1])
                        image.itemset((y, x, 2), values[i + 2])
                        i += 3

                # show image
                cv2.imshow("NAO's Vision top-camera-320x240", image)
        videoClient.unsubscribe(videoClient)

        """
        videoClient.setParam(18, 0)  # "kCameraSelectID", 0 : camera top, 1 : camera bottom
        resolution = 0  # 0 : QQVGA, 1 : QVGA, 2 : VGA
        colorSpace = 11  # RGB
        videoClient = videoClient.subscribe("python_client", resolution, colorSpace, 5)
        from_video = videoClient.getImageRemote(videoClient)
        imageWidth, imageHeight = from_video[0], from_video[1]

        for i in range(0, fps):
            # Grab the image (it is not a BGR, but a RGB)
            print("Image ", i, "captured")
            from_video = videoClient.getImageRemote(videoClient)
            img_nao = from_video[6]
            img_PIL = Image.fromstring("RGB", (imageWidth, imageHeight), img_nao)
            img_brute = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
            cv2.imshow("NAO's Vision top-camera-320x240", img_brute)

            time.sleep(0.1)

        videoClient.unsubscribe(videoClient)
        """
        return "Success"
    except Exception as ex:
        return str(ex)


if __name__ == '__main__':
    connect()
    app.run(debug=True, port=9000, use_reloader=False)
