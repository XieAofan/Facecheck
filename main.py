import module.rstp as rstp
import module.Dlib_face_cut as dfc
import base64
import cv2
import time
import _thread

def cv2_base64(image):
    base64_str = cv2.imencode('.jpg',image)[1].tostring()
    base64_str = base64.b64encode(base64_str)
    return base64_str

def get_img_from_camera_net():
    global frame
    cap = cv2.VideoCapture("rtsp://admin:xth88245228@192.168.2.3:554/ch1/main/av_stream")#获取网络摄像机
    while True:
        ret, frame = cap.read()
    cap.release()
    #cv2.imshow("capture", frame)
    #cv2.destroyAllWindows()

b=0
frame = ''
def main():
    global frame
    while True:
        t1 = time.time()
        img = frame
        n, faces =dfc.cut(img)
        if n > 0:
            t = 0
            for face in faces:
                t = t + 1
                b = b + 1 
                cv2.imshow('face_'+str(b), face)
                cv2.imwrite('D:\face\face_'+str(t)+'.jpg', face)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        t2 = time.time()
        print(str((t2-t1)*1000)+'ms')

if __name__ == '__main__':
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
