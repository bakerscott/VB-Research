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
	
def showFrame(frameTitle, frame):
	
	'''
	This function takes a single frame, and shows it on the computer
	
	In Values:
	frame = the frame that you wish to view.
	
	Out Values:
	none
	'''
	
	resize = cv2.resize(frame, (1200, 800)) 
	cv2.imshow(frameTitle, resize)
	cv2.waitKey(0)
	cv2.destroyAllWindows
	
	
def showAllFrames(vidName, frameList):
	
	'''
	This function takes in a list of frames, and shows the user all of them, in order
	
	In Values:
	frameList = The list of frames you wish to view.
	
	Out Values:
	none
	'''
	
	for i in range(len(frameList)):
		showFrame(vidName, frameList[i])

def foregroundOnly(videoName):
	
	'''
	This function takes in a video, applies an open cv2 mask to the image, and returns only the foreground of the videos, in grayscale.
	
	In Values:
	videoName = The name of whatever video you wish to read.
	
	Out Values:
	backSubList = The list of frames with all their background subtracted out.
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
		
		#fgmask = cv2.erode(fgmask, kernel)
		#fgmask = cv2.erode(fgmask, kernel)
		fgmask = cv2.erode(fgmask, kernel)
		#fgmask = cv2.dilate(fgmask, kernel)
		fgmask = cv2.dilate(fgmask, kernel)
		fgmask = cv2.dilate(fgmask, kernel)
		fgmask = cv2.dilate(fgmask, kernel)
		fgmask = cv2.dilate(fgmask, kernel)
		#fgmask = cv2.medianBlur(fgmask, 5)
		#fgmask = cv2.medianBlur(fgmask, 5)
		
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

def backgroundOnly(colorFrames, noBackFrames):
	
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
		
	midIndex = len(colorFrames) / 2
	midFrame = colorFrames[midIndex]
	for i in range(len(midFrame)):
		for j in range(len(midFrame[i])):
			b, g, r = midFrame[i][j]
			total = r + g + b
			if(total != 0):
				continue
			else:
				for k in range(1, len(colorFrames)):
					if k == midIndex:
						continue
					bnot, gnot, rnot = colorFrames[k][i][j]
					totalnot = bnot + gnot + rnot
					if(totalnot != 0):
						midFrame[i][j] = [bnot, gnot, rnot]
						print "Changed Pixel: [{}, {}]".format(i, j)
						break
					else:
						continue
				
	
	#out.release()
	#cv2.destroyAllWindows()	
	cv2.imwrite("midBackgroundTest.jpg", midFrame)
		
	return midFrame
	
	
def bg_subtract(frame, fgbg):
	'''
	Function taken from Westin, which creates a mask to delete a background
	'''
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
	fgmask = fgbg.apply(frame)
	ret, fgmask = cv2.threshold(fgmask, 250, 255, 0)
    
    # Erosions, dilations, and median blur used to eliminate noisy single pixels and smooth contours
	fgmask = cv2.erode(fgmask, kernel)
	fgmask = cv2.erode(fgmask, kernel)
	fgmask = cv2.erode(fgmask, kernel)
	fgmask = cv2.dilate(fgmask, kernel)
	fgmask = cv2.dilate(fgmask, kernel)
	fgmask = cv2.dilate(fgmask, kernel)
	fgmask = cv2.dilate(fgmask, kernel)
	fgmask = cv2.dilate(fgmask, kernel)
	fgmask = cv2.medianBlur(fgmask, 5)
	fgmask = cv2.medianBlur(fgmask, 5)

	return fgmask
	
def booleanConvert(noBackFrames):
	for i in range(len(20)):
		for j in range(len(noBackFrames[i])):
			for k in range(len(noBackFrames[i][j])):
				pixel = noBackFrames[i][j][k]
				if(pixel > 0):
					pixel = 255
					
		print "Done with frame {}".format(i)
	return noBackFrames
	
		
	
def internetBackgroundImage(vidName, alpha, showResult = False):
	import numpy as np
	import cv2

	cap = cv2.VideoCapture(vidName)
	first_iter = True
	result = None
	
	while True:
		ret, frame = cap.read()
		if frame is None:
			break

		if first_iter:
			avg = np.float32(frame)
			first_iter = False
			
		cv2.accumulateWeighted(frame, avg, alpha)
		result = cv2.convertScaleAbs(avg)
		
	if showResult == True:
		cv2.imshow("result", result)
		
	cv2.imwrite("averaged_frame.jpg", result)
	cv2.waitKey(0)

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()	


def robustBackgroundFinder(vidName):
	'''The purpose of this function is to have a one stop shop for finding the background of an image.  I wanted to write function components in this function, and then 
	eventually expand them into several different functions.
	
	Parameters:
	vidName = Name of the video from which you wish to get the background!
	'''
	
	cap = cv2.VideoCapture(vidName)
	vidLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	
	kernelColor = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	fgbgColor = cv2.createBackgroundSubtractorMOG2()
	
	kernelGray = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	fgbgGray = cv2.createBackgroundSubtractorMOG2()
	
	colorFrameList = []
	grayFrameList = []
	fgColorList = []
	fgGrayList = []
	bgColorList = []
	bgGrayList = []
	
	
	for i in range(vidLength):
		_, frame = cap.read()
		colorFrameList.append(frame)
		
		grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayFrameList.append(grayFrame)
		
		fgmaskColor = fgbgColor.apply(frame)
		fgmaskColor = cv2.morphologyEx(fgmaskColor, cv2.MORPH_OPEN, kernelColor)
		
		fgmaskGray = fgbgGray.apply(grayFrame)
		fgmaskGray = cv2.morphologyEx(fgmaskGray, cv2.MORPH_OPEN, kernelGray)
		
		fgColorList.append(fgmaskColor)
		fgGrayList.append(fgmaskGray)
		
	recolorizedColorFG = colorFrameList
	recolorizedGrayFG = grayFrameList
	

	#This is where we make the list of all the frames, with the foreground removed.
	for i in range(len(recolorizedGrayFG)):
		print "Recolorizing Frame:", i
		for j in range(len(recolorizedGrayFG[i])):
			foreground = np.where(fgGrayList[i][j] > 0)
			for k in foreground:
				recolorizedColorFG[i][j][k] = 0
				recolorizedGrayFG[i][j][k] = 0
				
	'''
	showFrame("Recolorize Attempt", recolorizedGrayFG[4])
	showFrame("Re2", recolorizedGrayFG[5])
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	'''
				
				
				
	#Now we have a foreground of both the color and gray, we can try to get a full background!
	firstColorFrame = recolorizedColorFG[1]
	firstGrayFrame = recolorizedGrayFG[1]
	blackenedPixels = {}
	
	print "Adding all of First Frame's Pixels"
	for i in range(len(firstGrayFrame)):
		for j in range(len(firstGrayFrame[i])):
			if firstGrayFrame[i][j] == 0:
				print "FF: Added [{}, {}, {}]".format("1", i, j)
				blackenedPixels["1, {}, {}".format(i, j)] = True
	
	print "Adding all other pixels"
	
	for i in range(2, len(recolorizedGrayFG)):
		print "On Frame {}".format(i)
		
		for j in range(len(recolorizedGrayFG[i])):
			#print "Frame: {}, row: {}".format(i, j)
			
			for k in range(len(recolorizedGrayFG[i][j])):
				key = "{}, {}, {}".format(i, j, k)
				if recolorizedGrayFG[i][j][k] == 0:
					if blackenedPixels.get(key):
						continue
					
					blackenedPixels[key] = True
					firstGrayFrame[j][k] = 0
					firstColorFrame[j][k] = 0
					
	
	'''
	showFrame("wut", firstGrayFrame)
	cv2.imwrite("backgroundAttempt.jpeg", firstGrayFrame)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	'''
	
	onlyBackground = firstGrayFrame
	
	secondAttempt = firstGrayFrame
	
	for i in range(len(firstGrayFrame)):
		blackSpaceInRow = np.where(firstGrayFrame[i] == 0)
		for pixel in blackSpaceInRow[0]:
			averagedPixel = 0
			counter = 0
			pixelList = []
			for j in range(1, len(grayFrameList)):
				if blackenedPixels.get("{}, {}, {}".format(j, i, pixel)):
					continue 
					
				pixelList.append(grayFrameList[j][i][pixel])
				averagedPixel = averagedPixel + grayFrameList[j][i][pixel]
				counter += 1
				
			if counter == 0:
				continue
				
			#print "Changing Pixel: [{}, {}] from {} to {}".format(i, pixel, onlyBackground[i][pixel], averagedPixel / counter)
			onlyBackground[i][pixel] = averagedPixel / counter
				
			pixelList = np.array(pixelList)
			pixSTD = np.std(pixelList)
			pixMax = np.amax(pixelList)
			print pixSTD, pixMax
			
			secondAvg = 0
			secondCounter = 0
			
			for i in range(len(pixelList)):
				if pixelList[i] < (pixMax - (3 * pixSTD)):
					print "Max: {}, STD: {}, Diff: {}, Current Pixel: {}".format(pixMax, pixSTD, (pixMax - pixSTD), pixelList[i])
					continue
					
				print "Adding pixel"
				secondAvg += pixelList[i]
				secondCounter += 1
				
			if secondCounter == 0:
				continue
				
			secondAttempt[i][pixel] = secondAvg / secondCounter
			
			
		
	#showFrame("Hopefully This Works", onlyBackground)
	cv2.imwrite("SecondAttempt.jpeg", secondAttempt)
	#cv2.imwrite("OnlyBackground.jpeg", onlyBackground)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()
		
		
	cap.release()
	
	return colorFrameList, grayFrameList, fgColorList, fgGrayList, bgColorList, bgGrayList

		
		
	

def main():
	#colorFrameList = readVideo("Hitter3-1.mp4")
	#grayFrameList = readVideo("Hitter1-2.mp4", gray = True)
	#noBack = foregroundOnly("Hitter3-1.mp4")
	
	#foreground = recolorize(colorFrameList, noBack)
	#showAllFrames(foreground)
	
	#onlyBack = backgroundOnly(colorFrameList, noBack)
	#showFrame(onlyBack)
	
	#booleanFrames = booleanConvert(noBack)
	
	#showAllFrames(booleanFrames)
	
	#internetBackgroundImage("Hitter3-1.mp4", .8)
	
	fl, gfl, fgcl, fggl, bgcl, bggl = robustBackgroundFinder("Hitter3-1.mp4")
	
	#showAllFrames("Video", fl)
	#showAllFrames("Gray Video", gfl)
	#showAllFrames("ForeGround of Color", fgcl)
	#showAllFrames("Foreground of Gray", fggl)
	#showAllFrames("Background of Color", bgcl)
	#showAllFrames("Background of Gray", bggl)
	
	
	
	return 0
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
