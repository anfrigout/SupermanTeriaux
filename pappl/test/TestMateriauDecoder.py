# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest
import json

from script import Materiau
from script import CustomDecoder
from script import MateriauEncoder

class TestMateriauDecoder(unittest.TestCase):
    """
    Classe pour tester la classe MateriauDecoder.
    Objectif : Vérifier le fonctionnement du decodage d'un fichier JSON
    Pré-requis : L'encoder MateriauEncoder doit être fonctionnel.
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
        json_str = json.dumps(materiau1, cls=MateriauEncoder.MateriauEncoder)
        materiau2 = CustomDecoder.CustomDecoder().decode(json_str)
        materiau_temoin = Materiau.Materiau()
        self.assertFalse(materiau1.equals(materiau_temoin))
        self.assertTrue(materiau1.equals(materiau2))

    def test_fichier_incorrect(self):
        """
        Test du décodage d'un fichier invalide.
        """
        json_str = json.dumps(dict(test="test", test2="test2"))
        self.assertRaises(KeyError, lambda: CustomDecoder.CustomDecoder().decode(json_str))


if __name__ == '__main__':
    unittest.main()
