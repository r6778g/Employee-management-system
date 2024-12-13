from google.colab.patches import cv2_imshow
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    if(ret==False):
        break
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2_imshow(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
