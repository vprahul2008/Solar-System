
import cv2

img = cv2.imread("ss.jpg")

cv2.putText(img,"Sun",(99,44),fontFace=5,fontScale=3,color=(13, 134,255 ))
cv2.putText(img,"Mercury",(110,272),fontFace=3,fontScale=1,color=(171, 170, 167))
cv2.putText(img,"Venus",(150,160),fontFace=3,fontScale=1,color=(5,181,240))
cv2.putText(img,"Earth",(272,272),fontFace=3,fontScale=1,color=(255,0,2))
cv2.putText(img,"Mars",(360,162),fontFace=3,fontScale=1,color=(75, 12,247 ))
cv2.putText(img,"Jupiter",(467,60),fontFace=3,fontScale=2,color=(0, 71, 143))
cv2.putText(img,"Saturn",(720,100),fontFace=3,fontScale=2,color=(156,202,217))
cv2.putText(img,"Uranus",(920,300),fontFace=3,fontScale=1,color=( 214,188,133))
cv2.putText(img,"Neptune",(1080,100),fontFace=3,fontScale=1,color=(240,77,85))
cv2.putText(img,"Solar System",(277,402),fontFace=2,fontScale=3,color=(255,255,255))

cv2.imshow("solar-system.jpg",img)
print(img)
cv2.waitKey(0)
