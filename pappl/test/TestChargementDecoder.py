# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest
import json

from script import Chargement
from script import CustomDecoder
from script import ChargementEncoder

class TestChargementDecoder(unittest.TestCase):
    """
    Classe pour tester la classe ChargementDecoder.
    Objectif : Vérifier le fonctionnement du decodage d'un fichier JSON
    Pré-requis : L'encoder ChargementEncoder doit être fonctionnel.
    """

    def test_fonctionnement_nominal(self):
        """
        Test du décodage d'un fichier correct.
        """
        chargement1 = Chargement.Chargement("NOM",
                                            1, 2, 3,
                                            4, 5, 6)
        json_str = json.dumps(chargement1, cls=ChargementEncoder.ChargementEncoder)

        chargement2 = CustomDecoder.CustomDecoder().decode(json_str)
        chargement_temoin = Chargement.Chargement()
        self.assertFalse(chargement1.equals(chargement_temoin))
        self.assertTrue(chargement1.equals(chargement2))

    def test_fichier_incorrect(self):
        """
        Test du décodage d'un fichier invalide.
        """
        json_str = json.dumps(dict(test="test", test2="test2"))
        self.assertRaises(KeyError, lambda: CustomDecoder.CustomDecoder().decode(json_str))


if __name__ == '__main__':
    unittest.main()
