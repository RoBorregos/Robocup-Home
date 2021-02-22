#! /usr/bin/env python
from __future__ import print_function

import csv
import json
from math import degrees, radians
import tf

import actionlib
import rospy
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

from nav_actions.go_to import goToAction
from nav_actions.move_base import MoveBase
from nav_actions.search_room import searchRoom

import actions.msg

""" 
Valid states:
    PENDING
    ACTIVE
    SUCCEEDED
    ABORTED
Valid Actions:
    gt-Place
    so-Object
    ao-toDefine
"""
class navigationServer(object):
    # Create messages that are used to publish feedback/result
    _feedback = actions.msg.navServFeedback()
    _result = actions.msg.navServResult()

    def __init__(self, name):
        self._action_name = name
        rospy.loginfo(name)
        # Initialize Navigation Action Server
        self._as = actionlib.SimpleActionServer(self._action_name, actions.msg.navServAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
    
    def execute_cb(self, goal):
        # Action Type
        action = goal.target_location[0:2]
 
        if action == "gt":
            # Validate target location
            rospy.loginfo("Goal received!")
            rospy.loginfo("Looking for the goal in the map...")
            goal_given = goal.target_location[3:] 
            self.executeGoToAction(goal_given)

        elif action == "so":
            #self.searchRoomAction = searchRoom()
            room_to_search = goal.target_location[3:]

            ## TODO check first if the goal room is the actual room
            ## if room != actual:
            ##    executeGoToAction(room_to_search)
            ##    
            self.executeSearchRoomAction(room_to_search)

            #rospy.loginfo("Search Object Action")

        elif action == "ao":
            rospy.loginfo("Approach Object Action")

        elif action == "cl":
            currentAction = moveBase()
            currentAction.cancelGoal()
            
        else:
            rospy.loginfo("Invalid Action")
            self._result = False
            self._as.set_aborted()
    
    def executeGoToAction(self, location):
        self.goToAction = goToAction()

        # Valid if the given location is in the known locations.
        if self.goToAction.locationExists(location) == True:
            # Start executing the action
            actionResult = self.send_goal(self.goToAction.getLocation(location))
            if actionResult:
                rospy.loginfo("You have reached the destination")
                self._result.result = True
                self._as.set_succeeded(self._result)
            else:
                rospy.loginfo("The robot failed to reach the destination")
                self._result.result = False
                self._as.set_aborted()
        else:
            #Rejected goal
            self._result = False
            rospy.loginfo('%s: Aborted. Location not found' % self._action_name)
            self._as.set_aborted()
    
    def executeSearchRoomAction(self, room):
        searchRoomAction = searchRoom()
        path = searchRoomAction.getGoalPoints(room)

        for goalPoint in path:
            result = self.send_goal(goalPoint)
            if (not result):
                rospy.loginfo("The robot failed to reach the destination")
                self._result.result = False
                self._as.set_aborted()
                return
            rospy.loginfo('Arrived to Goal Point')

        rospy.loginfo("You have reached the destination")
        self._result.result = True
        self._as.set_succeeded(self._result)
        ## loop over all goal points until end of room or object found
        ## for i in range(len(goalPoints)):
            ## self.send_goal(i)

    # Sets the server's feedback based on the move base feedback
    def setServerFeedback(self, data):
        #rospy.loginfo("list: %s", self.tf.getFrameStrings())

        #if self.tf.frameExists("/base_link") and self.tf.frameExists("/map"):
         #   rospy.loginfo("true")
          #  timeStamp = self.tf.getLatestCommonTime("/base_link", "/map")
           # currentPos, quat = self.tf.lookupTransform("/base_link", "/map", timeStamp)

        self._feedback.status = self._goal.getMoveBaseStatus(data)
        self._as.publish_feedback(self._feedback)
    
    def send_goal(self, goal_pose_given):
        rospy.loginfo(goal_pose_given)
        self._goal = MoveBase()
        self._goal.setGoal(goal_pose_given)
        self.tf = tf.TransformListener(True, rospy.Duration(3.0))
        
        # Create a topic listener of move_base node status
        moveBaseStatusTopic = rospy.Subscriber("move_base/status", GoalStatusArray, self.setServerFeedback)
        
        rospy.loginfo("Sending goal location ...")
        moveBaseState = self._goal.sendGoalToNavStack()
        moveBaseStatusTopic.unregister()

        return moveBaseState


if __name__ == '__main__':
    rospy.init_node('navServer')
    server = navigationServer(rospy.get_name())
    rospy.spin()
