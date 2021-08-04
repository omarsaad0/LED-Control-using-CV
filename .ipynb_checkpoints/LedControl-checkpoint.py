from cvzone.HandTrackingModule import HandDetector
import cv2
import cvzone
from cvzone.SerialModule import SerialObject
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)

mySerial = SerialObject("COM4", 9600, 1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
        mySerial.sendData(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
