import cv2
from django.shortcuts import render
from .models import GetCarImage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarImageSerializer
from camera.camera import LiveWebCam
from django.http.response import StreamingHttpResponse
# Create your views here.


    


def Home(request):
    car_images = GetCarImage.objects.all()
    return render(request, 'home.html', {'car_images': car_images})

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

@api_view(['POST'])
def addItem(request):
    serializer = CarImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

