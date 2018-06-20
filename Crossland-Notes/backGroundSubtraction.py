import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def readVideo(videoName, gray = False):
	vid = cv2.VideoCapture(videoName)
	vidLength = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
	frameList = []
	i = 0

	for j in range(vidLength):
		_, frame = vid.read()
		
		if gray == True:
			grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			frameList.append(grayFrame)
		else:
			frameList.append(frame)
    
	vid.release()
	return frameList
	
def showFrame(frame):
	resize = cv2.resize(frame, (1200, 800)) 
	cv2.imshow("frame", resize)
	cv2.waitKey(0)
	cv2.destroyAllWindows
	
	
def showAllFrames(frameList):
	for i in range(len(frameList)):
		showFrame(frameList[i])

def subtractFrame(videoName):
	
	'''
	plt.imshow(frame, cmap = "gray")
	plt.savefig("framePic.jpg")
	subFrame = nextFrame - frame
	with open("writeFile.txt", "w") as writeFile:
		for i in range(len(subFrame)):
			for j in range(len(subFrame[i])):
				writeFile.write("{} ".format(subFrame[i][j]))
			writeFile.write("\n")
			
	plt.imshow(subFrame, cmap = "gray")
	plt.savefig("preboolPic.jpg")
			
	for i in range(len(subFrame)):
		for j in range(len(subFrame[i])):
			if subFrame[i][j] >= alpha:
				subFrame[i][j] = 1
			else:
				subFrame[i][j] = 0
				
	with open("writeFile2.txt", "w") as writeFile:
		for i in range(len(subFrame)):
			for j in range(len(subFrame[i])):
				writeFile.write("{} ".format(subFrame[i][j]))
			writeFile.write("\n")
	
	plt.imshow(subFrame, cmap = "gray")
	plt.savefig("boolPic.jpg")
	'''
	
	vid = cv2.VideoCapture(videoName)
	vidLength = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
	
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	fgbg = cv2.createBackgroundSubtractorMOG2()
		
	backSubList = []
	
	for j in range(vidLength):
		_, frame = vid.read()
	
		fgmask = fgbg.apply(frame)
		fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
		
		backSubList.append(fgmask)
	
	vid.release()
	cv2.destroyAllWindows()
	
	return backSubList
	
def processEdges(frame):
	return cv2.Canny(frame, 200, 200)
	
'''
def createVideo(listOfFrames, vidName):
	out = cv2.VideoWriter(vidName, -1, 20.0, (1080, 1440))
	
	for i in range(len(listOfFrames)):
		frame = cv2.flip(listOfFrames[i],0)
		out.write(frame)
	out.release()
'''
			
	
	
def recolorize(colorFrames, noBackFrames):
	for i in range(len(colorFrames)):
		for j in range(len(colorFrames[i])):
			foreGround = noBackFrames[i][j] > 0
			for k in range(len(foreGround)):
				if(foreGround[k] == False):
					colorFrames[i][j][k] = 0
					
		print "Done with Frame {}".format(i)
		
	return colorFrames
		
	
	
def main():
	colorFrameList = readVideo("Hitter5-1.mp4")
	grayFrameList = readVideo("Hitter1-2.mp4", gray = True)
	noBack = subtractFrame("Hitter5-1.mp4")
	#showAllFrames(colorFrameList)
	#showAllFrames(grayFrameList)
	#showAllFrames(noBack)
	
	foreground = recolorize(colorFrameList, noBack)
	showAllFrames(foreground)
	
	return 0
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
