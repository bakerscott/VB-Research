import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import math



class StillFrame:
    
#     Initialization
    def __init__(self,iImage):
        self.image = iImage
#         self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        
#     Converting a color of a single frame
#     CAREFUL: make sure you are dealing with the correct type!
    def convertColor(self):
        self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        return self.image
    
    
#     Function for displaying a stillFrame instance
    def display(self):
        plt.imshow(self.image)
        
        
        
#     Useless currently
    def displayWidth(self,change):
        self.imageWidth = change
        print(self.imageWidth)
        
        
#     Useless currently
    def displayHeight(self,change):
        self.imageHeight = change
        print(self.imageHeight)