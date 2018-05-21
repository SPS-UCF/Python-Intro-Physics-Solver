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
	Plots the distance related to time initial velocity and acceleration
	:param initial_velocity:
	:param acceleration:
	:param time:

	:return:
	"""
	
	x_vals = np.linspace(0, time, 100)
	y_vals = km.distance_helper(initial_velocity, acceleration, x_vals)
	
	plt.plot(x_vals, y_vals)
	plt.plot(x_vals[-1], y_vals[-1], 'ro', label="Final Distance")
	plt.title("Distance over time")
	plt.xlabel("Time")
	plt.ylabel("Distance")
	
	plt.legend(('Initial Velocity: {}'.format(initial_velocity), 'Final Distance: {}'.format(y_vals[-1])), frameon=False)
	
	plt.show()
