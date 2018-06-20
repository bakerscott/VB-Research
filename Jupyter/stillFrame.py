import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import math



class StillFrame:
    
    def __init__(self,iImage):
        self.image = iImage
        # self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        
    def convertColor(self):
        self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        return self.image
    
    
    def display(self):
        plt.imshow(self.image)
        
        
    def displayWidth(self,change):
        self.imageWidth = change
        print(self.imageWidth)
        
    def displayHeight(self,change):
        self.imageHeight = change
        print(self.imageHeight)