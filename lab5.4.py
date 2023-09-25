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
	output=np.empty((240,320,3),dtype=np.uint8)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)
image=image[:,:,::-1]
window_name = 'Edge AI- Tiny Yolo'
cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)
image2=np.empty((240,320,3),dtype=np.uint8)
acc_x=0
acc_y=0
acc_count=0
for x in range (0,240):
	for y in range (0,320):
		b,g,r=image[x,y]
		if r>g and r>b:
			acc_x+=x
			acc_y+=y
			acc_count+=1
			image[x,y]=0,0,0


#cv2.namedWIndow('imageWindow',cv2.WINDOW_AUTOSIZE)
#cv2.imshow('imageWindow',stream)
#cv2.waiKey(0)
#cv2.destoyAllWindows()
if acc_count>0:
	mean_x=(acc_x/acc_count)
	mean_y=(acc_y/acc_count)
	mean_x=numpy.floor(mean_x)
	mean_y=numpy.floor(mean_y)
	image[int(mean_x)+0,int(mean_y)-1]=0,0,255
	image[int(mean_x)-1,int(mean_y)+0]=0,0,255
	image[int(mean_x)+0,int(mean_y)+0]=0,0,255
	image[int(mean_x)+1,int(mean_y)+0]=255,0,0
	image[int(mean_x)+0,int(mean_y)+1]=255,0,0
window_name2 = 'Edge AI- Tiny Yolo2'
cv2.imshow(window_name2, image)
raw_key = cv2.waitKey(20000)



