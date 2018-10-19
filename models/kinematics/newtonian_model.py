"""
Created on 10/19/17

Model for newtonian physics.

In this module are functions that are associated with the basic kinematic equations in physics 1. These functions
calculate either the distance or velocity given initial conditions of time/distance acceleration, and initial velocity.

Currently this module needs to be expanded to find more than just the final distance and velocity. Ideally, eventually
it will be expanded to include equations to solve for initial conditions or different final conditions.

"""

from models.kinematics import kinematic_plotting as kplt
import numpy as np


def distance(initial_velocity, acceleration, time):
	"""
	Calculates the distance traveled given the initial velocity, acceleration, and time then plots the distance traveled
	with respect to time.
	
	:param initial_velocity: Integer initial velocity
	:param acceleration: Integer acceleration
	:param time: Integer time
	
	:return: Integer distance traveled
	"""
	
	kplt.distance_plotter(initial_velocity, acceleration, time)
	
	return distance_helper(initial_velocity, acceleration, time)


def distance_helper(initial_velocity, acceleration, time):
	"""
	Calculates the distance traveled given the initial velocity, acceleration, and time, Helper function to the distance
	function.

	:param initial_velocity: Integer initial velocity
	:param acceleration: Integer acceleration
	:param time: Integer time
	
	:return: Integer distance traveled
	"""
	dist = initial_velocity * time + 0.5 * (acceleration * time ** 2)
	return dist


def vel_final_dist(initial_velocity, acceleration, dist):
	"""
	Calculates the final velocity given the initial velocity, acceleration and the distance traveled. Then plots the
	final velocity as a function of distance.
	
	:param initial_velocity: Integer initial velocity
	:param acceleration: Integer acceleration
	:param dist: Integer distance traveled
	
	:return: final velocity
	"""
	kplt.vel_final_dist_plotter(initial_velocity, acceleration, dist)

	return vel_final_dist_helper(initial_velocity, acceleration, dist)


def vel_final_dist_helper(initial_velocity, acceleration, dist):
	"""
	Calculates the final velocity given the initial velocity, acceleration and the distance traveled. And is a helper
	function to be called by vel_final_dist()

	:param initial_velocity: Integer initial velocity
	:param acceleration: Integer acceleration
	:param dist: Integer distance traveled

	:return: final velocity
	"""
	vel = (initial_velocity ** 2 + 2 * acceleration * dist) ** 0.5
	return vel


def vel_final_time(initial_velocity, acceleration, time):
	"""
	Calculates the final velocity given the initial velocity, acceleration, and time traveled. Then plots the final
	velocity as a function of time.
	
	:param initial_velocity: Integer initial velocity
	:param acceleration: Integer acceleration
	:param time: Integer time spent in air
	
	:return: final velocity
	"""
	kplt.vel_final_time_plotter(initial_velocity, acceleration, time)

	return vel_final_time_helper(initial_velocity, acceleration, time)


def vel_final_time_helper(initial_velocity, acceleration, time):
	"""
	Calculates the final velocity given the initial velocity, acceleration, and time traveled. This is a helper function
	for the vel_final_time function.

	:param initial_velocity: Integer initial velocity
	:param acceleration: Integer acceleration
	:param time: Integer time spent in air

	:return: final velocity
	"""
	vel = initial_velocity + acceleration * time
	return vel


def horizontal_range(initial_velocity, angle, g=9.81):
	"""
	Find the range of the particle based on the angle of launch and initial velocity. Then plots the trajectory of the
	particle.
	
	:param initial_velocity: Integer initial velocity
	:param angle: Integer launch angle
	:param g: Integer acceleration due to gravity

	:return: Range
	"""

	kplt.trajectory_plotter(initial_velocity, angle, g)

	return horizontal_range_helper(initial_velocity, angle, g)


def horizontal_range_helper(initial_velocity, angle, g=9.81):
	"""
	Find the range of the particle based on the angle of launch and initial velocity. This is a helper function for the
	horizontal_range function.

	:param initial_velocity: Integer initial velocity
	:param angle: Integer launch angle in degrees
	:param g: Integer acceleration due to gravity

	:return: Range
	"""

	horizon_range = initial_velocity ** 2 * np.sin(2 * np.deg2rad(angle)) / g
	return horizon_range


def maximum_height(initial_velocity, angle, initial_height=0, g=9.81):
	"""
	Finds the maximum height of the particle given the launch angle and the initial velocity, then plots the trajectory
	of the particle.

	:param initial_velocity: Integer initial velocity
	:param angle: Integer launch angle in degrees
	:param initial_height: Integer initial height, default 0
	:param g: Float acceleration due to gravity

	:return: Max Height
	"""

	kplt.trajectory_plotter(initial_velocity, angle, g, initial_height)

	return maximum_height_helper(initial_velocity, angle, g=g)


def maximum_height_helper(initial_velocity, angle, initial_height=0, g=9.81):
	"""
	Finds the maximum height of the particle given the launch angle and the initial velocity. This is a helper function
	to the maximum_height function.

	:param initial_velocity: Integer initial velocity
	:param angle: Integer launch angle in degrees
	:param initial_height: Integer initial height, default 0
	:param g: Integer acceleration due to gravity, default 9.81

	:return: Max Height
	"""
	max_height = (initial_velocity ** 2 * np.sin(np.deg2rad(angle)) ** 2) / (g * 2)
	return max_height
