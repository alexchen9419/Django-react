import cv2
import time
import threading
from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
import numpy as np

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.grabbed, self.frame = self.video.read()
        self.stopped = False
        
    def __del__(self):
        self.video.release()
        
    def start(self):
        threading.Thread(target=self.update, args=()).start()
        return self
        
    def update(self):
        while True:
            if self.stopped:
                self.video.release()
                return
            self.grabbed, self.frame = self.video.read()
            
    def stop(self):
        self.stopped = True
            
    def get_frame(self):
        _, jpeg = cv2.imencode('.jpg', self.frame)
        return jpeg.tobytes()
        
    def get_grayscale_frame(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        _, jpeg = cv2.imencode('.jpg', gray)
        return jpeg.tobytes()

# 全局相機對象
camera = None

def get_camera():
    global camera
    if camera is None:
        camera = VideoCamera().start()
    return camera

def gen_frames(camera, grayscale=False):
    while True:
        try:
            if grayscale:
                frame = camera.get_grayscale_frame()
            else:
                frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            time.sleep(0.1)  # 控制幀率
        except Exception as e:
            print(f"相機錯誤: {e}")
            break

# 5. 顯示攝影機畫面的視圖
def camera_view(request):
    return render(request, 'camera_stream/camera.html')

def camera_stream(request):
    camera = get_camera()
    return StreamingHttpResponse(gen_frames(camera),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# 6. 顯示灰階處理後的攝影機畫面
def grayscale_view(request):
    return render(request, 'camera_stream/grayscale.html')

def grayscale_stream(request):
    camera = get_camera()
    return StreamingHttpResponse(gen_frames(camera, grayscale=True),
                                 content_type='multipart/x-mixed-replace; boundary=frame')