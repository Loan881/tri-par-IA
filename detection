import cv2
import numpy as np

# Ouvrir la caméra
cap = cv2.VideoCapture(0)

# Attendre 2 secondes que la caméra se stabilise
cv2.waitKey(2000)

# Capturer image du tapis VIDE (référence)
ret, frame_reference = cap.read()
if not ret:
    print("Erreur caméra")
    exit()

frame_reference_gray = cv2.cvtColor(frame_reference, cv2.COLOR_BGR2GRAY)
frame_reference_gray = cv2.GaussianBlur(frame_reference_gray, (21, 21), 0)

print("Référence enregistrée. Détection en cours...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Conversion en niveau de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Différence entre tapis vide et image actuelle
    diff = cv2.absdiff(frame_reference_gray, gray)
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # Agrandir les zones blanches
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Trouver contours
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    objet_detecte = False

    for contour in contours:
        if cv2.contourArea(contour) > 5000:  # seuil à ajuster
            objet_detecte = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if objet_detecte:
        cv2.putText(frame, "PLASTIQUE DETECTE", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        print("Objet détecté sur le tapis !")

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
