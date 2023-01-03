# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest
import script.DatabaseTools

class TestDatabaseTools(unittest.TestCase):
    """
    Classe de test de la classe DatabaseTools
    """

    def test_executeSelect(self):
        """
        Ce test à pour objectif de tester la méthode executeSelect.
        """

        query = """SELECT * FROM 
        (SELECT * FROM public.materiau WHERE materiau.nom = %s) AS foo
        limit 1
        """
        data = ["ACIER"]
        reponse = script.DatabaseTools.DatabaseTools().executeSelect(query, data)
        self.assertEqual(1, len(reponse))

    def test_executeInsert(self):
        """
        Ce test à pour objectif de tester la méthode executeInsert
        """

        query = """SELECT count(1) FROM public.materiau"""
        avant = int(script.DatabaseTools.DatabaseTools().executeSelect(query)[0][0])
        query2 = """
        INSERT INTO public.materiau(nom, reference, e1, e2) VALUES (%s, %s, %s, %s)
        """
        data = ["QUALIF", "QUALIF", "1", "1"]
        script.DatabaseTools.DatabaseTools().executeInsert(query2, data)
        apres = int(script.DatabaseTools.DatabaseTools().executeSelect(query)[0][0])
        self.assertEqual(avant, apres-1)


if __name__ == '__main__':
    unittest.main()
