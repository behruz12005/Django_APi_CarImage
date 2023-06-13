
import cv2
import numpy as np
from django.conf import settings
from ultralytics import YOLO

model = YOLO("./media/model/best (2).pt", "v8")

def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)

    cx = x + x1
    cy = y + y1
    return cx, cy

class LiveWebCam(object):
	def __init__(self):
		self.url = cv2.VideoCapture("rtsp://admin:Pa$$123456@45.9.231.152:1041/ISAPI/Streaming/Channels/102")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,frame1 = self.url.read()
		detect_params = model.predict(source=[frame1], conf=0.45, save=False)
		resize = cv2.resize(frame1, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		
		return jpeg.tobytes()
		