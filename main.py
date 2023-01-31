# Open webcam, detect moment, capture moment as an image
# Will send image as email in the emailing.py

import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(3)

first_frame = None

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    cv2.imshow("My video", delta_frame)

    cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)



    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()