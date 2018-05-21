#!/usr/bin/env python
"""
Created on 10/19/17

Model for newtonian physics.

Here are some quick functions written, untested and is really just to put something up to modify and evolve from.
"""

import math
from models.kinematics import kinematic_plotting as plt


def distance(initial_vel, accl, time):
	"""
	Calculates the distance traveled given the initial velocity, acceleration, and time
	
	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param time: Integer time
	
	:return: Integer distance traveled
	"""
	
	plt.distance_plotter(initial_vel, accl, time)
	
	return distance_helper(initial_vel, accl, time)

def distance_helper(initial_vel, accl, time):
	"""
	Calculates the distance traveled given the initial velocity, acceleration, and time, Helper function to the distance
	function.

	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param time: Integer time
	
	:return: Integer distance traveled
	"""
	dist = initial_vel * time + 0.5 * (accl * time ** 2)
	return dist

def vel_final_dist(initial_vel, accl, dist):
	"""
	Calculates the final velocity given the initial velocity, acceleration and the distance traveled.
	
	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param dist: Integer distance traveled
	
	:return: final velocity
	"""
	vel = (initial_vel ** 2 + 2 * accl * dist) ** 0.5
	return vel
	
	
def vel_final_time(initial_vel, accl, time):
	"""
	Calculates the final velocity given the initial velocity, acceleration, and time traveled.
	
	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param time: Integer time spent in air
	
	:return: final velocity
	"""
	vel = initial_vel + accl * time
	return vel
	
	
def horizontal_range(initial_vel, angle, g=9.81):
	"""
	Find the range of the particle based on the angle of launch and initial velocity.
	
	:param initial_vel: Integer initial velocity
	:param angle: Integer launch angle
	:param g: Integer acceleration due to gravity

	:return: Range
	"""
	horizon_range = initial_vel ** 2 * math.sin(2 * angle) / g
	return horizon_range
