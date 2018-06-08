# VB-Research
Summer work for a volleyball video tracking project with Dr. David Knox at University of Colorado, Boulder

### Contributors:
* Crossland Beer
* Scott Baker

### Folders:
* Jupyter -- Contains official lab notebook and other assorted workbooks
* Information -- Contains updated version of project proposal, requirements, and schedule

## Action Items:
* [MAIN] assess viability of single lens camera accuracy
* Read all of the articles in the folder
* (s) get old code "running"/understood
* (s) manually work with an image to get "accurate height"

## Log:

#### Fri. 6/8:
* Meeting at 1pm with Knox to discuss proposal
  * updated requirements and questions added by Crossland to the `Summer-Work-Proposal-v2.pdf` in the `Information` folder
  * goal for next week: accuracy of a single lens fixed frame camera -- hand and computer calculation
* Scott: worked with basic OpenCV functionality regarding filters and identifiers

* Still researching descrepancies in the height of a player relative to a known object when the player is in a "jumping frame"
  * possible fix/estimate: use the trajectory or dimensional pixel variances of things we know (court lines)

#### Thu. 6/7:
* Scott and Crossland worked on the official project requirements and questions proposal -- to be submitted 6/8 1pm to Knox
  * Included:
    * Main questions to answer
    * Requirements and preliminary restrictions
    * Additional questions that could be answered through research
    * General weekly calendar with notable events and primary objectives
* Scott worked on Req. 1.1, a by-hand calculation of distance from fixed-frame single lens image
  * Successful in calculating a distance based on pixel length of a reference vs. actual objects
  * Shortcomings:
    * Initially, this algorithm requires that the base of the object-of-interest be coplanar with the reference object.
      * This is an issue because if we are measuring how high a player jumps, the player at max-height will not be on the same plane as the base of the pole (reference object)
    * Further research will be done to see the viability of a non-coplanar comparison
  * After mastering OpenCV, this hand-calculation will be done with an image of a player to test centimeter accuracy
  * More research should be done with using a standard (from initial calculation) Homography mapping of the 2-D image to 3-D space.

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
* Outline plan for week -- revolves around proposal
* Worked with Crossland on GitHub familiarity


# Notes:
This section can be deleted after acceptance of the project proposal.

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
