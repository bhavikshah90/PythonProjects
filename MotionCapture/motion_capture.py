import cv2, time, pandas
from datetime import datetime
from bokeh.plotting import figure
from bokeh.io import output_file,show

first_frame = None # variable to store first frame to capture start time
video = cv2.VideoCapture(0)
status_list = [None,None]
time_now = []
df = pandas.DataFrame(columns = ["Start","End"])
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

    cnts, hierachy=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    status_list = status_list[-2:]  # to avoid memory leakage problem because we just need to store last two status to track time

    if status_list[-1] == 1 and status_list[-2] == 0:
        time_now.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time_now.append(datetime.now())

    cv2.imshow("currently capturing ",gray_img)
    cv2.imshow("diff_frame",diff_frame)
    cv2.imshow("threshold", threshold_frame)
    cv2.imshow("color", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            time_now.append(datetime.now())
        break

for times in range(0,len(time_now),2):
    df=df.append({"Start":time_now[times],"End":time_now[times+1]},ignore_index=True)
df.to_csv("TimeTracker.csv")
print(df)
video.release()
cv2.destroyAllWindows()