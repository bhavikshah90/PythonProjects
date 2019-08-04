import cv2, time
first_frame = None # variable to store first frame to capture start time
video = cv2.VideoCapture(0)
while True:
    check,frame = video.read()
    status = 0

    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img,(21,21),0)

    if first_frame is None:
        first_frame = gray_img
        continue
    diff_frame = cv2.absdiff(first_frame,gray_img)
    threshold_frame = cv2.threshold(diff_frame,30,255,cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame,None,iterations = 2)

    (_,cnts,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)



    cv2.imshow("currently capturing ",gray_img)
    cv2.imshow("diff_frame",diff_frame)
    cv2.imshow("threshold", threshold_frame)
    cv2.imshow("color", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()