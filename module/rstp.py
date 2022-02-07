import cv2
def get_img_from_camera_net():
    cap = cv2.VideoCapture("rtsp://admin:xth88245228@192.168.2.3:554/ch1/main/av_stream")#获取网络摄像机
    ret, frame = cap.read()
    cap.release()
    #cv2.imshow("capture", frame)
    #cv2.destroyAllWindows()
    return frame

# 测试
if __name__ == '__main__':
    img= get_img_from_camera_net()
    cv2.imshow('one', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()