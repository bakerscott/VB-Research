import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import math
import stillFrame

class Clip:
    
    def __init__(self, filePath):
        # constructor, initilization
        self.cap = cv2.VideoCapture(filePath)
        
        
     
        
    def createFrames(self):
#         splitting up the video into frames
        self.frames = [] # this is the array of frames, might need to consider another data structure
        self.success, self.image = self.cap.read()
        self.count = 0
        self.success = True
        while self.success:
            self.success, self.image = self.cap.read()
#             print('Read a new frame',self.success)
            self.temp = stillFrame.StillFrame(self.image)
            self.frames.append(self.temp)
            self.count += 1
#             print(self.count)
#         printing the final count of frames, plus one for some reason
        print(self.count)
    
    
    
#     Function to convert ALL frames in the instance into RGB (looking normal)
#     NOTE: this is the "framework/process" to apply to any filter
    def convertBGR2RGB(self):
        for i in range(0, self.count - 1):
#             uses the .convertColor function from a stillFrame instance
            self.frames[i] = stillFrame.StillFrame(self.frames[i].convertColor())
    
    
    
#     Function to show a certain frame in the array of stillFrames
    def showFrame(self, number):
#         uses the .display function from a stillFrame instance
        self.frames[number].display()
        
        
#         useless, currently
    def getFrame(self, number):
        return self.frames[number]
    
    
#     still needs work
    def showVideo(self):
        
        
        while(True):
            print('true')
            # Capture frame-by-frame
            self.ret, self.frame = self.cap.read()
            
            if self.ret == True:
                print('true2')
                # Our operations on the frame come here
                self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
    
                # Display the resulting frame
                plt.imshow('frame',self.frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print('false2')
                break
        # When everything done, release the capture

        self.cap.release()
        cv2.destroyAllWindows()
        print('done')
        