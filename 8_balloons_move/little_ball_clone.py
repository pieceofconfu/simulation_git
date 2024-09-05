

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelState

class MoveObject:
    def __init__(self):
        rospy.init_node('move_object_node_little_clone', anonymous=True)
        self.object_pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)

    def move_to_position(self, x, y, z):
    
        object_state = ModelState()
        object_state.model_name = "little_ball_clone"
        object_state.pose.position.x = x
        object_state.pose.position.y = y
        object_state.pose.position.z = z

        object_state.pose.orientation.w = 1.0
        object_state.twist.linear.x = 0.0
        object_state.twist.linear.y = 0.0
        object_state.twist.linear.z = 0.0
        object_state.twist.angular.x = 0.0
        object_state.twist.angular.y = 0.0
        object_state.twist.angular.z = 0.0
        object_state.reference_frame = "world"  

        self.object_pub.publish(object_state)
        rospy.loginfo("Nesne belirtilen konuma taşındı.")

if __name__ == '__main__':
    try:

        move_object_node = MoveObject()

        x = -3
        y = 3
        z = 1
        pay = 0.0005
        while 1==1:    
            # (-3,3) - (3,3) aralığı    
            while x <= 3 and y >= 3:
                x = x + pay
                z = 1
                move_object_node.move_to_position(x, y, z)
                if x >= 3 and y >= 3:
                    break
                
            # (3,3) - (3,0) aralığı
            while x >= 3 and y >= 0 :
                y = y - pay
                z = 1
                move_object_node.move_to_position(x, y, z)
                if x >= 3 and y <= 0:
                    break
                
            # (3,0) - (0,-3) aralığı
            while x > 0 and y > -3:
                x = x - pay
                y = y - pay
                z = 1
                move_object_node.move_to_position(x, y, z)
                if x < 0 and y < -3:
                    break

            # (0,-3) - (-3,-3) aralığı
            while x > -3  and y < -3  :
                x = x - pay
                z = 1
                move_object_node.move_to_position(x, y, z)
                if x <= -3 and y <-3:
                    break
            
            # (-3,-3) - (-3,3) aralığı    
            while x <= -3 and y <= 3 :
                y = y + pay
                z = 1
                move_object_node.move_to_position(x, y, z)
                if x <= -3 and y >= 3:
                    break
            
        # move_object_node.move_to_position(x, y, z)

    except rospy.ROSInterruptException:
        pass
