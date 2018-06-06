# VB-Research
Summer work for a volleyball video tracking project with Dr. David Knox at University of Colorado, Boulder

# Contributors:
* Crossland Beer
* Scott Baker

# Folders:
* Jupyter

# Goals:
* Write a paper
* Learn/master GitHub
* Gain experience in Jupyter, Python, OpenCV, TensorFlow(?), Teletype Atom, etc.

# Action Items:
* [IMPORTANT] create a "summer Requirements and Questions proposal" --- due Friday 1pm Knox
* Read all of the articles in the folder
* (s) get old code "running"/understood
* (s) calendar with "work hours" and schedule and share it
* (s) manually work with an image to get "accurate height"

# Log:

#### Wed. 6/6:
* Read/Found article on getting height measurements from a video using "minimal calibration" (no dual-image)
  * Process found in article needs to be tested to see "centimeter accuracy"
* Propose (?) two parts to processing a "hit/play" video IF accurate:
  * height/distance detection based on gym "lines" and a fixed (standard) pole height
    * use image classification of image elements
    * algorithm for:
      * player height
      * ball height
  * track ball over multiple frames for a "trajectory"
* Steps:
  * manually get "height measurement algorithm" to work on an image (by hand) and assess accuracy
  * implement with OpenCV libraries to put height on player and/or volleyball
  * explore the "ball trajectory" tracking and overlay with height calculations

#### Tues. 6/5:
* Outline plan for week -- revloves around proposal
* Worked with Crossland on GitHub familiarity


# Notes:

## Questions:
* What elements of previous work can be used?
* What aspects of court/pixel size and relationship can we use for distances?
  * Can information about the court be used to find distances?
* What tracking are we able to do given a certain piece of hardware?
* What angles are "appropriate" for taking video of players?
* Can we use this to build and track volleyball images?
* (ultimate) Can we create a 3D model of a "hit/play/game"?

## Requirements:
* Some way to measure distance from camera to ball / players
* Know how high the player jumps
* Know how fast the player hits the volleyball
* Know the trajectory of the ball in flight


### Tracking:
* Centimeter accuracy of volleyball size and movement
* Given: specific angle and camera used

### Application:
second part of the project---application to recruiting and practical player evaluation
