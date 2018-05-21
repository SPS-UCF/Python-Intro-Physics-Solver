#!/usr/bin/env python
"""
Created by alex 
on 5/20/18

This module includes functions controlling the plotting of the kinematic functions.
"""
from matplotlib import pyplot as plt
from models.kinematics import newtonian_model as km
import numpy as np


def distance_plotter(initial_velocity, acceleration, time):
	"""
	Plots the distance related to time initial velocity and acceleration.

	:param initial_velocity: initial velocity of the object
	:param acceleration: Acceleration of the object
	:param time: Time for the object

	:return: None
	"""

	x_vals = np.linspace(0, time, 100)
	y_vals = km.distance_helper(initial_velocity, acceleration, x_vals)

	plt.plot(x_vals[-1], y_vals[-1], 'ro', label="Final Distance")
	plt.plot(x_vals, y_vals)
	plt.title("Distance over time")
	plt.xlabel("Time")
	plt.ylabel("Distance")

	plt.text(-0.25, y_vals[90], "Initial Velocity: {}".format(initial_velocity))
	plt.text(-0.25, y_vals[85], "Acceleration: {}".format(acceleration))
	plt.legend(('Final Distance: {}'.format(y_vals[-1]), 'Distance'), frameon=False)

	plt.show()

	return None


def vel_final_dist_plotter(initial_velocity, acceleration, dist):
	"""
	Plots the final velocity based on the distance given an initial velocity and acceleration.

	:param initial_velocity: Initial velocity
	:param acceleration: acceleration
	:param dist: Distance

	:return: None
	"""
	x_vals = np.linspace(0, dist, 100)
	y_vals = km.vel_final_dist_helper(initial_velocity, acceleration, x_vals)

	plt.plot(x_vals, y_vals)
	plt.plot(x_vals[-1], y_vals[-1], 'ro', label="Final Velocity")
	plt.title("Velocity over distance")
	plt.xlabel("Distance")
	plt.ylabel("Velocity")

	plt.text(-0.1, y_vals[85], "Initial Velocity: {}".format(initial_velocity))
	plt.text(-0.1, y_vals[80], "Acceleration: {}".format(acceleration))
	plt.legend(('Final Velocity: {}'.format(y_vals[-1]), 'Final Velocity'), frameon=False)

	plt.show()

	return None


def vel_final_time_plotter(initial_velocity, acceleration, time):
	"""
	Plotter function to plot the final velocity given time. It also plots the initial conditions of the problem.

	:param initial_velocity: Initial Velocity
	:param acceleration: Acceleration
	:param time: Time

	:return: None
	"""

	x_vals = np.linspace(0, time, 100)
	y_vals = km.vel_final_time_helper(initial_velocity, acceleration, x_vals)

	plt.plot(x_vals[-1], y_vals[-1], 'ro', label="Final Velocity")
	plt.plot(x_vals, y_vals)
	plt.title("Velocity over time")
	plt.xlabel("Time")
	plt.ylabel("Velocity")

	plt.text(-0.25, y_vals[85], "Initial Velocity: {}".format(initial_velocity))
	plt.text(-0.25, y_vals[80], "Acceleration: {}".format(acceleration))
	plt.legend(('Final Velocity: {}'.format(y_vals[-1]), 'Final Velocity'), frameon=False)

	plt.show()

	return None


def trajectory_plotter(initial_velocity, angle, g, initial_height=0):
	"""
	Plotter function that plots the trajectory of the particle with the inputted conditions.

	:param initial_velocity: Initial Velocity
	:param angle: Launch Angle
	:param g: Acceleration due to gravity
	:param initial_height: Integer initial height, default 0


	:return: None
	"""

	initial_y_velocity = initial_velocity * np.sin(np.deg2rad(angle))
	t_rise = initial_y_velocity / g

	t_fall = (2 * km.maximum_height_helper(initial_velocity, angle, g) / g) ** 0.5

	t_flight = t_fall + t_rise
	t_vals = np.linspace(0, t_flight, 100)

	x_vals = np.linspace(0, km.horizontal_range_helper(initial_velocity, angle, g), 100)

	y_vals = initial_height + initial_y_velocity * t_vals - (0.5 * g * t_vals ** 2)

	plt.plot(x_vals[50], y_vals[np.argmax(y_vals)], 'ro', label='Max Height')
	plt.plot(x_vals[-1], y_vals[-1], 'yo', label='Range')
	plt.plot(x_vals, y_vals, label='Trajectory')

	plt.title("Particle Trajectory")
	plt.xlabel("Distance")
	plt.ylabel("Height")

	plt.text(x_vals[25], y_vals[4], "Initial height: {}".format(initial_height))
	plt.text(x_vals[25], y_vals[5], "Initial Velocity: {}".format(initial_velocity))
	plt.text(x_vals[25], y_vals[6], "Acceleration due to gravity: {}".format(g))
	plt.legend(('Max height: {}'.format(y_vals[np.argmax(y_vals)]), 'Range: {}'.format(x_vals[-1])), frameon=False)

	plt.show()

	return None
