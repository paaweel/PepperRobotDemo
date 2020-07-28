import time
from PIL import Image
import numpy as np
from cv2 import cv2
from flask import Flask, request, Response
import qi
from multiprocessing import Process
from videoWrapper import VideoWrapper



app = Flask('video_service')

videoWrapper = VideoWrapper()


def capture():
    print("Capturing started")
    while True:
	a = 10

@app.route('/video', methods=['GET'])
def watch():
    try:
	"""
	# returns last 10 frames
        global video_service
        resolution = 2 	# VGA
        colorSpace = 11	# RGB
        fps = 20
        videoClient = video_service.subscribe("python_client", resolution, colorSpace, fps)
        print 'getting images in remote'	
        result = video_service.getImageRemote(videoClient)

        # create image
        width = result[0]
        height = result[1]
        image = np.zeros((height, width, 3), np.uint8)
	im = Image.frombytes("RGB", (width, height), image)
	im.show()
	iteration = 0

        while iteration < 10:
	    iteration=iteration+1
            # get image
            result = video_service.getImageRemote(videoClient)

            if result == None:
                print 'cannot capture.'
            elif result[6] == None:
                print 'no image data string.'
            else:
		image = str(bytearray(result[6]))
		im = Image.frombytes("RGB", (width, height), image)

    		im.show()

        video_service.unsubscribe(videoClient)
	"""
        return "Success"
    except Exception as ex:
        return str(ex)

@app.route('/start', methods=['POST'])
def startwatch():
    try:
	# videoWrapper.client = videoWrapper.video_service.subscribe(
	#	"python_client", 
	#	videoWrapper.resolution, 
	#	videoWrapper.colorSpace, 
	#	videoWrapper.fps)
	videoWrapper.captureFrames = True
	videoWrapper.process.start()
	return "Success"
    except Exception as ex:
        return str(ex)
	

@app.route('/stop', methods=['POST'])
def stopwatch():
    try:
	# videoWrapper.client.unsubscribe(videoClient)
	videoWrapper.captureFrames = False
	videoWrapper.process.join()
        return "Success"
    except Exception as ex:
        return str(ex)

if __name__ == '__main__':
    app.run(debug=True, port=9000, use_reloader=False)
