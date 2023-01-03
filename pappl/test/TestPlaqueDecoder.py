# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest
import json

from script import Materiau
from script import Pli
from script import Plaque
from script import CustomDecoder
from script import PlaqueEncoder

class TestPlaqueDecoder(unittest.TestCase):
    """
    Classe pour tester la classe PlaqueDecoder.
    Objectif : Vérifier le fonctionnement du decodage d'un fichier JSON
    Pré-requis : L'encoder PlaqueEncoder doit être fonctionnel.
    """

    def test_fonctionnement_nominal(self):
        """
        Test du décodage d'un fichier correct.
        """
        materiau1 = Materiau.Materiau("NOM", "REF",
                                      1, 2,
                                      3,
                                      4,
                                      5, 6,
                                      7, 8,
                                      9,
                                      10)
        materiau2 = Materiau.Materiau("NOM1", "REF1",
                                      11, 12,
                                      13,
                                      14,
                                      15, 16,
                                      17, 18,
                                      19,
                                      110)
        pli1 = Pli.Pli(45,
                      materiau1,
                      0.25,
                      1,
                      [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
                      [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
                      [[31, 32, 33], [34, 35, 36], [37, 38, 39]],
                      [[41, 42, 43], [44, 45, 46], [47, 48, 49]],
                      [[51, 52, 53], [54, 55, 56], [57, 58, 59]])
        pli2 = Pli.Pli(90,
                       materiau2,
                       1.25,
                       2,
                       [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
                       [[111, 112, 113], [114, 115, 116], [117, 118, 119]],
                       [[121, 122, 123], [124, 125, 126], [127, 128, 129]],
                       [[131, 132, 133], [134, 135, 136], [137, 138, 139]],
                       [[141, 142, 143], [144, 145, 146], [147, 148, 149]],
                       [[151, 152, 153], [154, 155, 156], [157, 158, 159]])
        plaque1 = Plaque.Plaque()
        plaque1.ajoutePli(pli1, 1)
        plaque1.ajoutePli(pli2, 1)
        self.assertEqual(len(plaque1.getListePlis()), 2, "Erreur création plaque")
        json_str = json.dumps(plaque1, cls=PlaqueEncoder.PlaqueEncoder)
        plaque2 = CustomDecoder.CustomDecoder().decode(json_str)
        json_str = json.dumps(plaque2, cls=PlaqueEncoder.PlaqueEncoder)

    def test_fichier_incorrect(self):
        """"
        Test du décodage d'un fichier invalide.
        """
        json_str = json.dumps(dict(test="test", test2="test2"))
        self.assertRaises(KeyError, lambda: CustomDecoder.CustomDecoder().decode(json_str))


if __name__ == '__main__':
    unittest.main()
