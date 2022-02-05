import dlib
import numpy as np
import cv2
import time

def cut(img):
    # Dlib 正向人脸检测器
    detector = dlib.get_frontal_face_detector()

    # 检测人脸
    faces = detector(img, 1)

    print("人脸数 / Faces in all:", len(faces))

    face_all = []
    for k, d in enumerate(faces):

        # 计算矩形大小

        # 计算矩形框大小
        height = d.bottom()-d.top()
        width = d.right()-d.left()

        # 根据人脸大小生成空的图像
        img_blank = np.zeros((height, width, 3), np.uint8)

        for i in range(height):
            for j in range(width):
                    img_blank[i][j] = img[d.top()+i][d.left()+j]
        face_all.append(img_blank)
        # cv2.imshow("face_"+str(k+1), img_blank)
    return len(faces), face_all


if __name__ == '__main__':
    t1 = time.time()
    p = input()
    n, img = cut(cv2.imread(str(p)))
    t2 = time.time()
    print((t2-t1))
    t = 0
    for i in img:
        t = t + 1
        cv2.imwrite('cut_'+str(t)+'.jpg', i)
    print("finish")
