"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import csv
from tkinter import * 
from gaze_tracking import GazeTracking
import threading
ret = False

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
b=lr=ll=lc=0
def thread_function():
    global ret
    cap = cv2.VideoCapture('Funny.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
   
# Closes all the frames
def eye_gaze():
    global b,lr,ll,lc
    x = threading.Thread(target=thread_function)
    x.start()
    
    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()
        print(ret)
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)
    
        frame = gaze.annotated_frame()
        text = ""
    
        if gaze.is_blinking():
            text = "Blinking"
            b=b+1
        elif gaze.is_right():
            text = "Looking right"
            lr=lr+1
        elif gaze.is_left():
            text = "Looking left"
            ll=ll+1
        elif gaze.is_center():
            text = "Looking center"
            lc=lc+1
    
        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    
        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    
        cv2.imshow("Demo", frame)
    
        if cv2.waitKey(1) == 27 or ret == False:
            with open('Report.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                t=b+lr+lc+ll
                dt=b+lr+ll
                dp=(dt/t)*100
                cp=(lc/t)*100
                r=""
                print("csv")
                writer.writerow([b,lr,ll,lc,t,dp,cp,r])
            break
    
    webcam.release()
    cv2.destroyAllWindows()
    root = Tk()
    root.geometry("200x200")
    
    mylabel = Label(root, text = r, padx = 50, fg="red")
    mylabel.pack(pady=70)
    
    
    