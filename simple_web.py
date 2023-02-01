import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:

    st_img = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.now()

        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 255), thickness=2,
                    lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=now.strftime("%I:%M:%S %p"), org=(30, 110),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=2,
                    lineType=cv2.LINE_AA)


        st_img.image(frame)
