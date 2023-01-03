# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest

from script import Materiau
from script import Pli
from script import Plaque

class TestPli(unittest.TestCase):
    """
    Classe permettant de tester la classe pli
    """
    def test_matSouplesse(self):
        # Création du matériau de ref
        mat = Materiau.Materiau("NOM", "REF",
                                134000, 7000,
                                4200, 0.25,
                                -1400, -200,
                                1500, 50,
                                75)
        pli = Pli.Pli(0, mat, 0.5)
        pli.majMatSouplesse()
        pli.setOrientation(45)
        pli.majMatSouplesseBase()

    def test_matRigidite(self):
        mat = Materiau.Materiau("NOM", "REF",
                                134000, 7000,
                                4200, 0.25,
                                -1400, -200,
                                1500, 50,
                                75)
        pli = Pli.Pli(0, mat, 0.5)
        pli.majMatRigidite()
        pli.setOrientation(45)
        pli.majMatRigiditeBase()

    def test_majAllMatrices(self):
        mat = Materiau.Materiau("NOM", "REF",
                                134000, 7000,
                                4200, 0.25,
                                -1400, -200,
                                1500, 50,
                                75)
        pli1 = Pli.Pli(0, mat, 0.25, 1)
        pli2 = Pli.Pli(45, mat, 0.25, 2)
        pli3 = Pli.Pli(-45, mat, 0.25, 3)
        pli4 = Pli.Pli(90, mat, 0.25, 4)
        pli5 = Pli.Pli(45, mat, 0.25, 5)
        pli6 = Pli.Pli(0, mat, 0.25, 6)
        plaque = Plaque.Plaque()
        plaque.ajoutePli(pli1, 1)
        plaque.ajoutePli(pli2, 1)
        plaque.ajoutePli(pli3, 1)
        plaque.ajoutePli(pli4, 1)
        plaque.ajoutePli(pli5, 1)
        plaque.ajoutePli(pli6, 1)
        plaque.setZMin(-0.75)
        plaque.majMatrices()


if __name__ == '__main__':
    unittest.main()
