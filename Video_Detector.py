#!/usr/bin/python2.7

import cv2
import dlib

detector = dlib.simple_object_detector("WhiteSign_detector.svm")
win_det = dlib.image_window()
win_det.set_image(detector)

print("Showing detections on the in the folder.......")

ret = True
win = dlib.image_window()
vid = cv2.VideoCapture("untitled.mpg")
while(ret):
    #capture frame-by-frame
    ret, frame = vid.read()
    if ret == True:
        pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        dets = detector(pic)
        print("Number of road signs detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()
            ))
        win.clear_overlay()
        win.set_image(pic)
        win.add_overlay(dets)
    else:
        break

vid.release()