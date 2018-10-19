"""
Created by Alex Hopkins
on 5/17/18

Test cases for the newtonian model functions
"""
from models.kinematics.newtonian_model import *
import unittest


class TestNewtonian(unittest.TestCase):
	
	def test_distance(self):
		"""
		Simple test to assert the distance traveled for an object traveling with an initial velocity of 5 m/s at 2 m/s^2
		acceleration for 10 seconds will be 150 meters. This answer was calculated by hand.
		"""
		print(distance(5, 2, 10))
		self.assertEqual(distance(5, 2, 10), 150)
		
	def test_vel_final_dist(self):
		"""
		Simple test to check if the final velocity with a given initial velocity of 5 m/s at 2 m/s^2 acceleration with
		a distance traveled of 4m is within 3 decimal places of the hand calculated final velocity answer.
		"""
		print(vel_final_dist(5, 2, 4))
		self.assertAlmostEqual(vel_final_dist(5, 2, 4), 6.403, places=3)
	
	def test_vel_final_time(self):
		"""
		Simple test to assert the final velocity is 25 given the initial velocity of 5 m/s with an acceleration of 2 m/s^2
		for a time of 10 seconds. The test answer was calculated by hand.
		"""
		print(vel_final_time(5, 2, 10))
		self.assertEqual(vel_final_time(5, 2, 10), 25)
	
	def test_horizontal_range(self):
		"""
		Simple test to assert the horizontal range of a projectile given it's initial velocity and angle. Tested by hand
		with theta = 45 deg and initial velocity of 5 m/s
		"""
		print(horizontal_range(5, 45))
		self.assertAlmostEqual(horizontal_range(5, 45), 2.548, places=3)

	def test_maximum_height(self):
		"""
		Simple test to assert the maximum range of a projectile given it's initial velocity and angle. Tested by hand
		with theta = 45, and initial velocity = 5 m/s and g = 9.81 m/s^2. up to 3 decimal places
		"""
		print(maximum_height(5, 45))
		self.assertAlmostEqual(maximum_height(5, 45), 0.637, places=3)


if __name__ == '__main__':
	unittest.main()
