import cv2, time

video = cv2.VideoCapture(0)
while True:
    check,frame = video.read()
    print(check)
    print(frame)
    # time.sleep(3)
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("currently capturing ",gray_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()