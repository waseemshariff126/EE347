import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

stream=io.BytesIO()
with picamera.PiCamera() as camera:
	camera.resolution=(320,240)
	camera.framerate=24
	time.sleep(1)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)

window_name = 'Edge AI- Tiny Yolo'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)

for x in range (0,240):
	for y in range (0,320):
		r,g,b=image[x,y]
		if r>g and r>b:
			image[x,y]=255,0,0


window_name2 = 'Edge AI- Tiny Yolo2'
cv2.imshow(window_name2, image)
raw_key = cv2.waitKey(20000)
