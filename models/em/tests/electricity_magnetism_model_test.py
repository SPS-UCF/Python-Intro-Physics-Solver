"""
Created by Alex Hopkins
on 10/19/18

Electricity and magnetism model test functions
"""
import models.em.em_model as emm
import unittest


class TestEM(unittest.TestCase):

    def test_coulomb_force(self):
        """
        Tests the coulomb force between two charges. The asserted values are calculated by hand using the equation
        F = k * q_1 * q_2 / r ** 2
        """
        print(emm.coulomb_force(1.6e-19, -1.6e-19, 1))
        self.assertAlmostEqual(emm.coulomb_force(1.6e-19, -1.6e-19, 1), -2.3e-28, places=3)

    def test_n_electric_field(self):
        nq = 2
        emm.n_electric_field(nq)


if __name__ == '__main__':
    unittest.main()
