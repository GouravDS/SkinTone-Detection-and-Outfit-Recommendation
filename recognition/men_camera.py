import cv2
from django.conf import settings


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()


    #This function is used in views

    def get_frame(self):
        
        while True:    
            _, frame = self.video.read()
            hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
            height , width, _ = frame.shape

            cx = (350,100)
            cy = (280,125)
            cz = (0,0)
            pixel_center = hsv_frame[cx,cy,cz]
            hue_value = pixel_center[0]
            sat_value = pixel_center[0]
            value = pixel_center[0]
            color = "Undefined"
            if hue_value <= 2 and sat_value <= 35 and value <= 62:
                color="Camel"
            elif hue_value <= 6 and sat_value <= 50 and value <= 61:
                color="Tan"
            elif hue_value <= 9 and sat_value <= 50 and value <= 72:
                color="Antique Brass"
            elif hue_value <= 10 and sat_value <= 16 and value <= 71:
                color="Tuscany"
            elif hue_value <= 11 and sat_value <= 41 and value <= 67:
                color="Tumbleweed"
            elif hue_value <= 14 and sat_value <= 40 and value <= 53:
                color = "Pastle Brown"
            elif hue_value <= 15 and sat_value <= 43 and value <= 63:
                color="Blast-Off Bronze"
            elif hue_value <= 17 and sat_value <= 25 and value <= 92:
                color="Desert Sand"
            elif hue_value <= 19 and sat_value <= 75 and value <= 44:
                color="Liver (Organ)"
            elif hue_value <= 25 and sat_value <= 94 and value <= 84:
                color = "Tan"
            pixel_center_bgr = frame[cx, cy, cz]
            cv2.putText(frame,color,(10,50),0,1,(0,0,255),2)
            cv2.rectangle(frame, cx, cy, (255 , 255, 255), 3)
            cv2.imshow("Frame",frame)
            key = cv2.waitKey(1)
            if key == 27:
               break
            frame_fli = cv2.flip(frame,-1)
            frame_flip = cv2.rotate(frame_fli,cv2.ROTATE_180)
            ret, jpeg = cv2.imencode('.jpg', frame_flip)
            return jpeg.tobytes()

   