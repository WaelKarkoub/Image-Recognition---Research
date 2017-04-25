#!/usr/bin/python2.7

import os
import glob

import dlib
from skimage import io

detector = dlib.simple_object_detector("roadSign_detector.svm")
win_det = dlib.image_window()
win_det.set_image(detector)

print("Showing detections on the in the folder.......")

win = dlib.image_window()
for f in glob.glob(os.path.join("/home/wael-karkoub/Desktop/Research/Pictures/Random/", "*.jpg")):
    print("Processing file: {}".format(f))
    img = io.imread(f)
    dets = detector(img)
    print("Number of road signs detected: {}".format(len(dets)))
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()
        ))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    dlib.hit_enter_to_continue()
