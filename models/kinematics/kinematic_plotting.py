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

	plt.text(-0.25, 130, "Initial Velocity: {}".format(initial_velocity))
	plt.text(-0.25, 122, "Acceleration: {}".format(acceleration))
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

	plt.text(-0.1, 6.2, "Initial Velocity: {}".format(initial_velocity))
	plt.text(-0.1, 6.1, "Acceleration: {}".format(acceleration))
	plt.legend(('Final Velocity: {}'.format(y_vals[-1]), 'Final Velocity'), frameon=False)

	plt.show()

	return None
