import cv2
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
time.sleep(2)

ret, frame_ref = cap.read()
if not ret:
    print("Erreur caméra")
    exit()

gray_ref = cv2.cvtColor(frame_ref, cv2.COLOR_BGR2GRAY)
gray_ref = cv2.GaussianBlur(gray_ref, (21, 21), 0)

print("Détection en cours...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    diff = cv2.absdiff(gray_ref, gray)
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    objet_detecte = False

    for contour in contours:
        if cv2.contourArea(contour) > 5000:
            objet_detecte = True
            break

    if objet_detecte:
        print("Plastique détecté !")
        with open("signal.txt", "w") as f:
            f.write("PHOTO")
        time.sleep(2)

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
