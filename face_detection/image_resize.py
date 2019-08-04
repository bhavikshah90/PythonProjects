import cv2

img = cv2.imread("minions.jpg",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img,(200,500))
cv2.imshow("minions",resized_img)
cv2.imwrite("minions.resized.jpg",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
