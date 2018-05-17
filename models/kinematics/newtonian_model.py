#!/usr/bin/env python
"""
Created on 10/19/17

Model for newtonian physics.

Here are some quick functions written, untested and is really just to put something up to modify and evolve from.
"""

# Kinematics Equations
import math

def distance(initial_vel, accl, time):
	"""
	Calculates the distance traveled given the inital velocity acceleration and time
	
	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param time: Integer time
	
	:return: Integer distance traveled
	"""
	return initial_vel * time + 0.5 * (accl * time ** 2)

def vel_final_dist(initial_vel, accl, dist):
	"""
	Calcuates the final velocity given the initial velocity, acceleration and the distance traveled.
	
	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param dist: Integer distance traveled
	
	:return: final velocity
	"""
	return initial_vel ** 2 + 2 * accl * dist
	
	
def vel_final_time(initial_vel, accl, time):
	"""
	Calculates the final velocity given the initial velocity, acceleration, and time traveled.
	
	:param initial_vel: Integer initial velocity
	:param accl: Integer acceleration
	:param time: Integer time spent in air
	
	:return: final velocity
	"""
	return initial_vel + accl * time


def height(initial_vel, initial_h, g, time):
	"""
	Height function of time H(t) = - (1 / 2) g t 2 + Vo t + Ho
	
	:param initial_vel: Integer initial velocity
	:param initial_h: Integer initial height
	:param g: Integer acceleration due to gravity
	:param time: Integer input time
	:return: height
	"""
	return -(1/2) * g * time ** 2 + initial_vel * time + initial_h
	
	
def horizontal_range(initial_vel, g, angle):
	"""
	Find the range of the particle based on the angle of launch and initial velocity.
	
	:param initial_vel: Integer initial velocity
	:param g: Integer acceleration due to gravity
	:param angle: Integer launch angle
	
	:return: Range
	"""
	return initial_vel ** 2 * math.sin(2 * angle) / g
