import cv2
video=cv2.VideoCapture(0)
count=1
while True:
    success,img=video.read()
    cv2.imshow("Me",img)
    if cv2.waitKey(1)&0XFF==ord('q'):
        break
    elif cv2.waitKey(1)&0XFF==ord('s'):
        cv2.imwrite(f"photos/image{count}.png",img)
        print('Image Saved')
video.release()
