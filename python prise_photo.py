import cv2
import time
import os

cap = cv2.VideoCapture(0)

dossier = "photos"
if not os.path.exists(dossier):
    os.makedirs(dossier)

print("Programme photo prêt...")

while True:

    if os.path.exists("signal.txt"):

        ret, frame = cap.read()
        if ret:
            nom = f"{dossier}/photo_{int(time.time())}.jpg"
            cv2.imwrite(nom, frame)
            print(f"Photo prise : {nom}")

        os.remove("signal.txt")

    time.sleep(0.5)

cap.release()
