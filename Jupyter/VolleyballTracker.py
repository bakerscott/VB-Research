import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import math
from IPython.display import clear_output
#import sklearn
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
from sklearn.cluster import estimate_bandwidth


'''
variables:
cap -- VideoCapture object


'''


class VolleyballTracker:

    def __init__(self, filePath):
        # constructor, initilization
        self.cap = cv2.VideoCapture(filePath)

    def displayVideo(self):
        vid = self.cap
        try:
            while(True):
                ret, frame = vid.read()
                if not ret:
                    vid.release()
                    print("<released>")
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                plt.axis('on')
                plt.title("<Input Stream>")
                plt.imshow(frame)
                plt.show()
                clear_output(wait=True)
        except KeyboardInterrupt:
            vid.release()
            print("<released>")

        '''
        while(True):
            ret, frame = self.cap.read()

            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
                '''
