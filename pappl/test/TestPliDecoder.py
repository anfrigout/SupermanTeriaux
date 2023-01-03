# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest
import json

from script import Materiau
from script import Pli
from script import PliEncoder
from script import CustomDecoder


class TestPliDecoder(unittest.TestCase):
    """
    Classe pour tester la classe PliDecoder.
    Objectif : Vérifier le fonctionnement du decodage d'un fichier JSON
    Pré-requis : L'encoder PliEncoder doit être fonctionnel.
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
        pli1 = Pli.Pli(45,
                       materiau1,
                       0.25,
                       5,
                       [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                       [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
                       [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
                       [[31, 32, 33], [34, 35, 36], [37, 38, 39]],
                       [[41, 42, 43], [44, 45, 46], [47, 48, 49]],
                       [[51, 52, 53], [54, 55, 56], [57, 58, 59]])
        json_str2 = json.dumps(pli1, cls=PliEncoder.PliEncoder)
        pli2 = CustomDecoder.CustomDecoder().decode(json_str2)
        pli_temoin = Pli.Pli()
        self.assertFalse(pli1.equals(pli_temoin))
        self.assertTrue(pli1.equals(pli2), "Erreur decoder")

    def test_fichier_incorrect(self):
        """
        Test du décodage d'un fichier invalide.
        """
        json_str = json.dumps(dict(test="test", test2="test2"))
        self.assertRaises(KeyError, lambda: CustomDecoder.CustomDecoder().decode(json_str))


if __name__ == '__main__':
    unittest.main()
