import os
from emailing import send_email
import glob
import cv2
import time
from threading import Thread

# Open webcam, detect moment, capture moment as an image
# Will send image as email in the emailing.py


def clean_folder():
    print("Clean folder function started. ")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("Clean folder function ended. ")


video = cv2.VideoCapture(0)
time.sleep(2)

first_frame = None
status_list = []
count = 0

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]

    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 15000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/image{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images)/2)
            if all_images:
                main_image1 = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]
    print(status_list)

    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(main_image1, ))
        email_thread.daemon = True

        email_thread.start()

    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
clean_thread = Thread(target=clean_folder())
clean_thread.daemon = True
clean_thread.start()
