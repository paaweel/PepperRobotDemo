import time
from flask import Flask
from videoWrapper import VideoWrapper

app = Flask('video_service')

videoWrapper = VideoWrapper()


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
        videoWrapper.stopThread()
    finally:
        try:
            videoWrapper.startThread()
            return "Success"
        except Exception as ex:
            return str(ex)


@app.route('/stop', methods=['POST'])
def stopwatch():
    try:
        videoWrapper.stopThread()
        return "Success"
    except Exception as ex:
        return str(ex)


if __name__ == '__main__':
    app.run(debug=True, port=9000, use_reloader=False)
