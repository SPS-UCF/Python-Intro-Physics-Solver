"""
Created by Alex Hopkins
on 10/19/18

Model for Electricity and Magnetism.

In this module there are functions that calculate the basic questions of physics 2.
"""

import numpy as np


def coulomb_force(q1, q2, r):
    """
    Calculates the force between two point charges.

    Applying coulombs law of F = k * q_1 * q_2 / r ** 2 to find the force of attraction/repulsion between two charges
    based on their distance from each other.

    :param q1: Scalar: Charge given in Coulombs
    :param q2: Scalar: Charge given in Coulombs
    :param r: Scalar: Distance between two charges given in meters

    :return: Scalar: Force between the two charges, given as Newtons
    """

    k = 8.987e9     # N * m ** 2 / C ** 2

    force = k * (q1 * q2) / r ** 2
    return force
