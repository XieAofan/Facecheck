import rstp, cv2, time
import base64

def cv2_base64(image):
    base64_str = cv2.imencode('.jpg',image)[1].tostring()
    base64_str = base64.b64encode(base64_str)
    return base64_str

n, img = rstp.get_img_from_camera_net()

