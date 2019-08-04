import cv2
import glob

images = glob.glob("*.jpeg")
print(images)


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for i in images:
    img = cv2.imread(i)

    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray_img,(int(gray_img.shape[1]/3),int(gray_img.shape[0]/3)))
    faces = face_cascade.detectMultiScale(resized_img,
                                          scaleFactor=1.05,
                                          minNeighbors = 5)

    print (type(faces))
    print (faces)
    for x,y,w,h in faces:
        img = cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),3)
    # resized_output_img = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    cv2.imshow("updated_img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
