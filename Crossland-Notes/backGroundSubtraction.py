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


def robustBackgroundFinder(vidName, extension):
	'''
	The purpose of this function is to have a one stop shop for finding the background of an image.  I wanted to write function components in this function, and then 
	eventually expand them into several different functions.
	
	Parameters:
	vidName = Name of the video from which you wish to get the background!
	extension = The .extension of the video (.mp4, .avi, etc)
	
	Returns:
	colorFrameList = A list of the frames of the video, unedited, in color.
	grayFrameList = A list of the frames of the video, made gray.
	fgColorList = A list of all the color frames, with the background made black.
	blackAndWhiteForegroundOnly = A foreground only video, where the moving parts are white or gray and the background is black.
	'''
	
	#Loading the Video into the program, naming it cap.
	cap = cv2.VideoCapture(vidName + extension)
	vidLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #establishing the video length, to be used later.
	
	#creating the kernel and mask for the background subtractor.
	kernelColor = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	fgbgColor = cv2.createBackgroundSubtractorMOG2()
	
	kernelGray = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	fgbgGray = cv2.createBackgroundSubtractorMOG2()
	
	#Creating 4 lists, to be returned after manipulation.
	colorFrameList = []
	grayFrameList = []
	fgColorList = []
	fgGrayList = []
	blackAndWhiteForegroundOnly = []
	
	
	#This loop is used to go through the length of the video, and add every frame to the colorFrame list.
	for i in range(vidLength):
		_, frame = cap.read()
		colorFrameList.append(frame)
		
		#This section turns the color frames gray and adds them to grayFrameList
		grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayFrameList.append(grayFrame)
		
		#This applies our foreground mask, generating a black and white video, where the background is black, and the foreground is white.
		fgmaskColor = fgbgColor.apply(frame)
		fgmaskColor = cv2.morphologyEx(fgmaskColor, cv2.MORPH_OPEN, kernelColor)
		
		fgmaskGray = fgbgGray.apply(grayFrame)
		fgmaskGray = cv2.morphologyEx(fgmaskGray, cv2.MORPH_OPEN, kernelGray)
		
		fgGrayList.append(fgmaskGray)
		
		blackAndWhiteForegroundOnly.append(fgmaskColor)
		
	#This creates the output writer for the video with a colored foreground and a black background.
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('{}-blackBack{}'.format(vidName, extension),fourcc, 10.0, (1440, 1080))
	
	print "***Beginning process of creating foreground only video***"
	
	#This loop is used to create a video where the background is black, but the player and other moving parts are colored.
	fgColorList = colorFrameList
	for i in range(len(blackAndWhiteForegroundOnly)):
		print "Generating frame {} of {}-blackBack.mp4".format(i, vidName)
		for j in range(len(blackAndWhiteForegroundOnly[i])):
			blackSpace = np.where(blackAndWhiteForegroundOnly[i][j] == 0)
			blackSpace = blackSpace[0]
			for k in blackSpace:
				fgColorList[i][j][k] = 0
		if i == 0:
			continue
		out.write(fgColorList[i])
		
	out.release()
	
	#Now we have generated a video where only the foreground is colored, now we can move onto creating an image of only the background.
	
	recolorizedGrayFG = grayFrameList
	recolorizedColorFG = colorFrameList
	
	print "***Beginning process of finding background aggregate***"

	#This is where we make the list of all the frames, with the foreground removed.
	#This for loop for blacking out all moving parts in the colored video, so that we can create our aggregate and final background in the future.
	for i in range(len(recolorizedGrayFG)):
		print "Blacking out foreground from frame {} of {}{}".format(i, vidName, extension)
		for j in range(len(recolorizedGrayFG[i])):
			foreground = np.where(fgGrayList[i][j] > 0)
			for k in foreground:
				recolorizedGrayFG[i][j][k] = 0	
				recolorizedColorFG[i][j][k] = 0	
				
	print "***Beginning process of creating background aggregate***"
				
	#Now we have a foreground of both the color and gray, we can try to get a full background!
	firstColorFrame = recolorizedColorFG[1]
	firstGrayFrame = recolorizedGrayFG[1]
	blackenedPixels = {}
	
	#This for loop goes through our first frame, because it is being considered outside the rest of the video, and adds all the already blackened pixels to a
	#dictionary of pixels that do not need to be relooked at.
	
	print "Adding frame 1 to {}-backAgg.jpeg".format(vidName)
	for i in range(len(firstGrayFrame)):
		for j in range(len(firstGrayFrame[i])):
			if firstGrayFrame[i][j] == 0:
				#print "FF: Added [{}, {}, {}]".format("1", i, j)
				blackenedPixels["1, {}, {}".format(i, j)] = True
	
	#print "Adding all other pixels"
	
	#This for loop goes through, and finds all other black pixels in all other pictures in the video, and adds them to the dictionary, and if they are not already
	#added makes the corresponding pixel in the first frame black as well.
	for i in range(2, len(recolorizedGrayFG)):
		print "Adding frame {} to {}-backAgg.jpeg".format(i, vidName)
		
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
					
	#we then generate a picture with all the pixels in any frame that are black, all superimposed on the first frame.
	cv2.imwrite("{}-backAgg.jpeg".format(vidName), firstGrayFrame)
	
	onlyBackground = firstGrayFrame
	
	print "***Beginning process of creating our final background image***"
	
	#Now we have an aggregate of all the black pixels, and we can use that to generate our final background.
	#To do that, we average all other pixels that aren't black in every position where there is black in our aggregate.  We then replace the black pixel with the 
	#averaged pixel value!
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
		
	cv2.imwrite("{}-onlyBack.jpeg".format(vidName), onlyBackground)
		
	cap.release()
	
	return colorFrameList, grayFrameList, fgColorList, blackAndWhiteForegroundOnly

def edgeDetector(imageName, extension):
	fullImg = imageName + extension
	
	img = cv2.imread(fullImg, 0)
	edges = cv2.Canny(img,100,200)
	
	cv2.imwrite("{}-Edges.jpeg".format(imageName), edges)
	

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
	
	fl, gfl, fgcl, fggl, bgcl, bggl = robustBackgroundFinder("Hitter4-5", ".mp4")
	
	#showAllFrames("Video", fl)
	#showAllFrames("Gray Video", gfl)
	#showAllFrames("ForeGround of Color", fgcl)
	#showAllFrames("Foreground of Gray", fggl)
	#showAllFrames("Background of Color", bgcl)
	#showAllFrames("Background of Gray", bggl)
	
	#edgeDetector("5-1-bkOne", ".jpeg")
	
	
	
	return 0
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
