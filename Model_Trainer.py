#!/usr/bin/python2.7

import os
import sys
import glob

import dlib
from skimage import io

options = dlib.simple_object_detector_training_options()
options.C = 5
options.num_threads = 4
options.be_verbose = True

training_xml_path = os.path.join("/home/wael-karkoub/Desktop/Research/Codes/", "road_sign_trial.xml")
testing_xml_path = os.path.join("/home/wael-karkoub/Desktop/Research/Codes/", "road_sign_trial.xml")
dlib.train_simple_object_detector(training_xml_path, "roadSign_detector.svm", options)

print("")
print("Training accuracy : {}".format(dlib.test_simple_object_detector(training_xml_path,"roadSign_detector.svm")))
print("Testing accuracy : {}".format(dlib.test_simple_object_detector(testing_xml_path,"roadSign_detector.svm")))

