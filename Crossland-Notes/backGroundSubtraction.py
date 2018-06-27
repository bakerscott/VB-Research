import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def readVideo(videoName, gray = False):
	
	'''
	readVideo takes in a video, and converts it into a series of frames in a list, which is returned.
	
	In values:
	videoName = The name of the video in your file
	gray = A keyword argument for whether or not you want to make the video grayscale
	
	Out values:
	frameList = A list of the frames of the video, in order
	'''
	
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
	
	'''
	This function takes a single frame, and shows it on the computer
	
	In Values:
	frame = the frame that you wish to view.
	
	Out Values:
	none
	'''
	
	resize = cv2.resize(frame, (1200, 800)) 
	cv2.imshow("frame", resize)
	cv2.waitKey(0)
	cv2.destroyAllWindows
	
	
def showAllFrames(frameList):
	
	'''
	This function takes in a list of frames, and shows the user all of them, in order
	
	In Values:
	frameList = The list of frames you wish to view.
	
	Out Values:
	none
	'''
	
	for i in range(len(frameList)):
		showFrame(frameList[i])

def subtractFrame(videoName):
	
	'''
	This function takes in a video, applies an open cv2 mask to the image, and returns only the foreground of the videos, in grayscale.
	
	In Values:
	videoName = The name of whatever video you wish to read.
	
	Out Values:
	backSubList = The list of frames with all their background subtracted out.
	'''
	
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
	
'''
def processEdges(frame):
	return cv2.Canny(frame, 200, 200)
'''
				
def recolorize(colorFrames, noBackFrames):
	
	'''
	The purpose of this function is to take in a list of colored frames, and another list of their corresponding black and white, backgroundless frames,
	and only keep the parts of the colored frames that are visible in the backgroundless frames.
	
	In Values:
	colorFrames = A list of colored frames for any given video
	noBackFrames = A list of grayscale, backgroundless frames for any given video.
	
	Out Values:
	colorFrames = The same list of colored frames from above, but changed to only show where the color is in the backgroundless frames.
	'''
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('Hitter1-2-Fore.mp4',fourcc, 10.0, (1440, 1080))
	
	for i in range(len(colorFrames)):
		for j in range(len(colorFrames[i])):
			foreGround = noBackFrames[i][j] > 0
			for k in range(len(foreGround)):
				if(foreGround[k] == False):
					colorFrames[i][j][k] = 0
					
		print "Done with Frame {}".format(i)
		out.write(colorFrames[i])
	
	out.release()
	cv2.destroyAllWindows()	
		
	return colorFrames
	
'''
def recolorize2(vidName):
	cap = cv2.VideoCapture(vidName)
	fgbg = cv2.createBackgroundSubtractorMOG2()
	
	while True:
		ret, frame = cap.read()
		fgmask = fgbg.apply(frame)
		
		cv2.imshow("original", frame)
		cv2.imshow("Mask", fgmask)
		
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
			
	cap.release()
	cv2.destroyAllWindows()
'''

def onlyBackground(colorFrames, noBackFrames):
	
	'''
	This function is a 'first' attempt on giving an image with only the background in it.  It takes a list of colored frames, as well as a list of backgroundless
	frames, and uses them to generate an image with all the foreground blacked out.  Then, a second process goes through the first frame of the video, and finds all
	places where the video is black.  If it is, it searches for a place in another video where it is not black.  If it finds it, that pixel gets replaced with 
	a colored pixel and the function moves on.
	
	In Values:
	colorFrames = A list of colored frames for a given video
	noBackFrames = A list of frames with their backgrounds subtracted.
	
	Out Values:
	firstFrame = the first frame in the colored video which has been modified to only show the "background"
	'''
	
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	#out = cv2.VideoWriter('Hitter1-2-Back.mp4',fourcc, 10.0, (1440, 1080))
	
	for i in range(len(colorFrames)):
		for j in range(len(colorFrames[i])):
			foreGround = noBackFrames[i][j] > 0
			for k in range(len(foreGround)):
				if(foreGround[k] == True):
					colorFrames[i][j][k] = 0
					
		print "Done with Frame {}".format(i)
		#out.write(colorFrames[i])
		
	firstFrame = colorFrames[1]
	for i in range(len(firstFrame)):
		for j in range(len(firstFrame[i])):
			b, g, r = firstFrame[i][j]
			total = r + g + b
			if(total != 0):
				continue
			else:
				for k in range(2, len(colorFrames)):
					bnot, gnot, rnot = colorFrames[k][i][j]
					totalnot = bnot + gnot + rnot
					if(totalnot != 0):
						firstFrame[i][j] = [bnot, gnot, rnot]
						print "Changed Pixel: [{}, {}]".format(i, j)
						break
					else:
						continue
				
	
	#out.release()
	#cv2.destroyAllWindows()	
	cv2.imwrite("onlyBackground2.jpg", firstFrame)
		
	return firstFrame

		
	
	
def main():
	colorFrameList = readVideo("Hitter3-1.mp4")
	#grayFrameList = readVideo("Hitter1-2.mp4", gray = True)
	noBack = subtractFrame("Hitter3-1.mp4")
	#showAllFrames(colorFrameList)
	#showAllFrames(grayFrameList)
	#showAllFrames(noBack)
	
	#foreground = recolorize(colorFrameList, noBack)
	#showAllFrames(foreground)
	
	
	
	#recolorize2("Hitter3-1.mp4")
	
	onlyBack = onlyBackground(colorFrameList, noBack)
	showFrame(onlyBack)
	
	return 0
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
