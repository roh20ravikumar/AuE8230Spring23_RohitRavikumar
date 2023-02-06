The codes are all located in - assignment2_ws > src > turtlebot_ass > scripts
There is a folder inside scripts with some test files as well.

1) Circle.py: This code has to ru the turtle bot in a circle with specified linear velocity of 0.2 units/sec and aan angular velocity of 0.2 rads/sec.


2) square_openloop : A while loop is incorporated for the straight section. Time is first taken outside the loop and then once the loop is run, the current time is calculated for each iteration. The current distance will then be the - time insude the loop minus the time outside the loop multiplied by the velocity. The condition for the while loop to exit is if the current distance exceeds 0.2 units. The same logic is used for the rotation part. The turtle rotates till the angle - pi/2 rads or 90 degrees is achieved after which it can trace out the 2nd side of the square.
The inspiration for this code was: Moving in a straight line and Rotation on ROS Wiki:

http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line
http://wiki.ros.org/turtlesim/Tutorials/Rotating%20Left%20and%20Right


3) square_closedloop: for the closed loop, the Gotogoal code was used as the skeleton and some changes were made to run it as per our requirement. The Gotogoal code took a user input for the coordinates. For our requirement we had to automate the user input with an array which ran in a for loop and took new indices after every loop to complete the square.  The propotional constants were also tweaked to get the best performance. The K for the angle was increased to make the turtle turn fast and then facilitate a straight line with the K for the linear_vel.
The resource for this file was gotogoal on ROS Wiki:

http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal



RUNNING  THE CODE
1) Start ROSCORE
2) In another terminal window, simultaneously run the code below to open turtle sim
ROSRUN turtlesim turtlesim_node
3) In another terminal run the ROSRUN tuertlbot_ass2 ________(name of the file)

 Images and Videos are in the assignment_ws folder
