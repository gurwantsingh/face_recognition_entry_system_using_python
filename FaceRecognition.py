import cv2
import os
from deepface import DeepFace


allimages = os.listdir('photos')
vid = cv2.VideoCapture(0)
while True:
    frame = vid.read()[1]
    success, img = vid.read()
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        try:
            for i in allimages:
                result = DeepFace.verify(img1_path=f'photos/{i}', img2_path=frame)
                if result['verified'] is True:
                    self.finalImg = i
        except:
         print('Image not found')
    elif cv2.waitKey(1) & 0xFF==ord('q'):
     break







