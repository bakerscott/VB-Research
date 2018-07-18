import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import math
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