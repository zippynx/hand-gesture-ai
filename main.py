import cv2
import mediapipe as mp
import math
import numpy as np
import time

from volume_controller import volume, volMin, volMax


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

pTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            for id, lm in enumerate(handLms.landmark):

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                lmList.append((id, cx, cy))

                if id == 4 or id == 8:
                    cv2.circle(
                        img,
                        (cx, cy),
                        10,
                        (255, 0, 255),
                        cv2.FILLED
                    )

    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        # Convert distance to volume
        vol = np.interp(length, [30, 200], [volMin, volMax])

        # Volume percentage
        volPer = np.interp(length, [30, 200], [0, 100])

        # Volume bar
        volBar = np.interp(length, [30, 200], [400, 150])

        volume.SetMasterVolumeLevel(vol, None)

        # UI Volume Bar
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)

        cv2.rectangle(
            img,
            (50, int(volBar)),
            (85, 400),
            (255, 0, 0),
            cv2.FILLED
        )

        cv2.putText(
            img,
            f'{int(volPer)} %',
            (40, 450),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 0, 0),
            3
        )

    # FPS
    cTime = time.time()

    fps = 1 / (cTime - pTime)

    pTime = cTime

    cv2.putText(
        img,
        f'FPS: {int(fps)}',
        (40, 50),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (0, 255, 0),
        3
    )

    cv2.imshow("Hand Gesture Volume Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break