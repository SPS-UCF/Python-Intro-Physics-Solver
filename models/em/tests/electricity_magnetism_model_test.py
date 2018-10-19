"""
Created by Alex Hopkins
on 10/19/18

Electricity and magnetism model test functions
"""
from models.em.electricity_magnetism_model import *
import unittest


class TestEM(unittest.TestCase):

    def test_coulomb_force(self):
        """
        Tests the coulomb force between two charges. The asserted values are calculated by hand using the equation
        F = k * q_1 * q_2 / r ** 2
        """
        print(coulomb_force(1.6e-19, -1.6e-19, 1))
        self.assertAlmostEqual(coulomb_force(1.6e-19, -1.6e-19, 1), -2.3e-28, places=3)


if __name__ == '__main__':
    unittest.main()
