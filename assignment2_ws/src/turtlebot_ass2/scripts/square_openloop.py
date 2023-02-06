#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def square_straight1():
    # Starts a new node
    rospy.init_node('turtlesim', anonymous=True)
    #Define the publisher
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    i=0
    current_distance = 0 # current distance which should approach 2
    
    t0 = rospy.Time.now().to_sec() # current time before startinh the manouver
    
    #first straight
    while(current_distance <= 2):

      
       
        vel.linear.x = 0.2
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        pub.publish(vel)  # publishes the velocity 
        t1=rospy.Time.now().to_sec()  # current time in the loop
        current_distance = 0.2*(t1-t0)
     
    vel.linear.x = 0 # sets the vel back to 0
    pub.publish(vel)


     # now for rotation of 90 degrees       
    current_angle= 0
    t2 = rospy.Time.now().to_sec()
    
                
    while(current_angle<=1.5707963267948): # angle is in radians
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.2
            
        pub.publish(vel)
        t3 = rospy.Time.now().to_sec() # current time in the loop
        current_angle = 0.2*(t3-t2) # current angle
        
    vel.angular.z = 0
    pub.publish(vel)
    
    #2nd straight
    
    current_distance = 0
    t0 = rospy.Time.now().to_sec() 
    while(current_distance <= 2):

      
       
        vel.linear.x = 0.2
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
     
        pub.publish(vel) 
            
        t1=rospy.Time.now().to_sec()
            
        current_distance = 0.2*(t1-t0)
     
     
    vel.linear.x = 0
    pub.publish(vel)


            
    current_angle= 0
    t2 = rospy.Time.now().to_sec()
    
                
    while(current_angle<=1.5707963267948):
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.2
            
        pub.publish(vel)
        t3 = rospy.Time.now().to_sec()
        current_angle = 0.2*(t3-t2)
        
    vel.angular.z = 0
    pub.publish(vel)
    
    #3rd straight
    
    current_distance = 0
    t0 = rospy.Time.now().to_sec() 
    while(current_distance <= 2):

      
       
        vel.linear.x = 0.2
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
     
        pub.publish(vel) 
            
        t1=rospy.Time.now().to_sec()
            
        current_distance = 0.2*(t1-t0)
     
     
    vel.linear.x = 0
    pub.publish(vel)


            
    current_angle= 0
    t2 = rospy.Time.now().to_sec()
    
                
    while(current_angle<=1.5707963267948):
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.2
            
        pub.publish(vel)
        t3 = rospy.Time.now().to_sec()
        current_angle = 0.2*(t3-t2)
        
    vel.angular.z = 0
    pub.publish(vel)
    #4th Straight
    current_distance = 0
    t0 = rospy.Time.now().to_sec() 
    while(current_distance <= 2):

      
       
        vel.linear.x = 0.2
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
     
        pub.publish(vel) 
            
        t1=rospy.Time.now().to_sec()
            
        current_distance = 0.2*(t1-t0)
     
     
    vel.linear.x = 0
    pub.publish(vel)
      
	  
if __name__ == '__main__':
    try:
        #Testing our function
        square_straight1()
        
    except rospy.ROSInterruptException: pass
