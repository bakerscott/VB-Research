import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import math
import stillFrame

class Clip:
    
    def __init__(self, filePath):
        self.cap = cv2.VideoCapture(filePath)
        
        
        '''
        self.x = stillFrame.StillFrame()
        self.x.displayWidth(1001)
        self.x.displayHeight()
        '''
        
    def createFrames(self):
        self.frames = []
        self.success, self.image = self.cap.read()
        self.count = 0
        self.success = True
        while self.success:
            self.success, self.image = self.cap.read()
            # print('Read a new frame',self.success)
            self.temp = stillFrame.StillFrame(self.image)
            self.temp = self.temp.convertColor()
            self.frames.append(self.temp)
            self.count += 1
        print(self.count)
        
    def showFrame(self, number):
        self.frames[number].display()
        
    def getFrame(self, number):
        return self.frames[number]
    
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
        
    def f(self):
        print("Testing",self.i)
        print(str(self.i))
        
    def g(self):
        print("testing again")
        