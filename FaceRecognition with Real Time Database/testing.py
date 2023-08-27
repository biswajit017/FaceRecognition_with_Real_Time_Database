import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

background_path = "Resources/background.png"


folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList =[]
print(modePathList)
while True:
    success, img = cap.read()

    imgBackground[162:162 + 480, 55:55 + 640] = img

    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
