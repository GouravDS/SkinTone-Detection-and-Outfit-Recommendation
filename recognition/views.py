from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from recognition.men_camera import  VideoCamera
from recognition.women_camera import  VideoCameraa


# Create your views here.
def men(request):
	return render(request, 'recognition/men.html')

def women(request):
	return render(request, 'recognition/women.html')

## method for men camera..........
def gen(men_camera):
	while True:
		frame = men_camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')

### method for women camera.........
def gene(women_camera):
	while True:
		frame = women_camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_fee(request):
	return StreamingHttpResponse(gene(VideoCameraa()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')

## for women dress colour......
def Camel(request):
	return render(request, 'recognition/Camel.html')

def Tan(request):
	return render(request, 'recognition/Tan.html')

def Tumbleweed(request):
	return render(request, 'recognition/Tumbleweed.html')

def Antique_Brass(request):
	return render(request, 'recognition/Antique_Brass.html')

def Pastle_Brown(request):
	return render(request, 'recognition/Pastle_Brown.html')

def Desert_sand(request):
	return render(request, 'recognition/Desert_sand.html')

## for men dress colour......
def C(request):
	return render(request, 'recognition/C.html')

def T(request):
	return render(request, 'recognition/T.html')

def Tumb(request):
	return render(request, 'recognition/Tumb.html')

def A(request):
	return render(request, 'recognition/A.html')

def P(request):
	return render(request, 'recognition/P.html')

def D(request):
	return render(request, 'recognition/D.html')

def Tus(request):
	return render(request, 'recognition/Tus.html')

def B(request):
	return render(request, 'recognition/B.html')

def L(request):
	return render(request, 'recognition/L.html')
