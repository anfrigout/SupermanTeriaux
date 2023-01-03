# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import unittest
import script.Materiau
import script.DatabaseTools

class MyTestCase(unittest.TestCase):
    def test_gettters(self):
        """
        Ce test à pour objectif de tester les getters
        """
        mat = script.Materiau.Materiau("NOM_MAT", "MA_REF", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(mat.getNom(), "NOM_MAT", "Erreur getNom()")
        self.assertEqual(mat.getRef(), "MA_REF", "Erreur getRef()")
        self.assertEqual(mat.getE1(), 1, "Erreur getE1()")
        self.assertEqual(mat.getE2(), 2, "Erreur getE2()")
        self.assertEqual(mat.getG12(), 3, "Erreur getG12()")
        self.assertEqual(mat.getV12(), 4, "Erreur getV12()")
        self.assertEqual(mat.getS11_c(), 5, "Erreur getS11_c()")
        self.assertEqual(mat.getS22_c(), 6, "Erreur getS22_C()")
        self.assertEqual(mat.getS11_t(), 7, "Erreur getS11_t()")
        self.assertEqual(mat.getS22_t(), 8, "Erreur getS22_t()")
        self.assertEqual(mat.getS12(), 9, "Erreur getS12()")
        self.assertEqual(mat.getPourcentageFibre(), 10, "Erreur getPourcentageFibre()")

    def test_setters(self):
        """
        Ce test à pour objectif de tester le fonctionnement des setters.
        """

        mat = script.Materiau.Materiau()
        mat.setNom("TEST_NOM")
        mat.setRef("TEST_REF")
        mat.setE1(1)
        mat.setE2(2)
        mat.setG12(3)
        mat.setV12(4)
        mat.setS11_c(5)
        mat.setS22_c(6)
        mat.setS11_t(7)
        mat.setS22_t(8)
        mat.setS12(9)
        mat.setPourcentageFibre(10)
        self.assertEqual(mat.getNom(), "TEST_NOM", "Erreur setNom()")
        self.assertEqual(mat.getRef(), "TEST_REF", "Erreur setRef()")
        self.assertEqual(mat.getE1(), 1, "Erreur setE1()")
        self.assertEqual(mat.getE2(), 2, "Erreur setE2()")
        self.assertEqual(mat.getG12(), 3, "Erreur setG12()")
        self.assertEqual(mat.getV12(), 4, "Erreur setV12()")
        self.assertEqual(mat.getS11_c(), 5, "Erreur setS11_c()")
        self.assertEqual(mat.getS22_c(), 6, "Erreur setS22_C()")
        self.assertEqual(mat.getS11_t(), 7, "Erreur setS11_t()")
        self.assertEqual(mat.getS22_t(), 8, "Erreur setS22_t()")
        self.assertEqual(mat.getS12(), 9, "Erreur setS12()")
        self.assertEqual(mat.getPourcentageFibre(), 10, "Erreur setPourcentageFibre()")

    def test_clone(self):
        """
        Ce test à pour objectif de tester que la méthode clone permet de créer deux objets disctincts.
        """

        mat1 = script.Materiau.Materiau("NOM_MAT", "MA_REF", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        mat2 = script.Materiau.Materiau().clone(mat1)
        self.assertNotEqual(mat1, mat2, "Erreur les objets sont identiques.")
        self.assertEqual(mat2.getNom(), "NOM_MAT", "Erreur clone du nom.")
        self.assertEqual(mat2.getRef(), "MA_REF", "Erreur clone de la ref.")
        self.assertEqual(mat2.getE1(), 1, "Erreur clone de e1.")
        self.assertEqual(mat2.getE2(), 2, "Erreur clone de e2.")
        self.assertEqual(mat2.getG12(), 3, "Erreur clone de g12.")
        self.assertEqual(mat2.getV12(), 4, "Erreur clone de v12.")
        self.assertEqual(mat2.getS11_c(), 5, "Erreur clone de s11c.")
        self.assertEqual(mat2.getS22_c(), 6, "Erreur clone de s22c.")
        self.assertEqual(mat2.getS11_t(), 7, "Erreur clone de s11t.")
        self.assertEqual(mat2.getS22_t(), 8, "Erreur clone de s22t.")
        self.assertEqual(mat2.getS12(), 9, "Erreur clone de s12.")
        self.assertEqual(mat2.getPourcentageFibre(), 10, "Erreur clone de fibre.")

    def test_esuals(self):
        """
        Ce test vérifie le fonctionnement de la méthode equals.
        """

        mat1 = script.Materiau.Materiau("NOM_MAT", "MA_REF", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        mat2 = script.Materiau.Materiau().clone(mat1)
        mat3 = script.Materiau.Materiau()
        self.assertTrue(mat1.equals(mat2))
        self.assertFalse(mat1.equals(mat3))

    def test_ajouteDatabase(self):
        """
        Ce test vérifie l'ajout d'un matériau dans la base de données.
        """

        mat = script.Materiau.Materiau("QUALIF_NOM", "QUALIF_REF", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        query = """SELECT count(1) FROM public.materiau"""
        avant = int(script.DatabaseTools.DatabaseTools().executeSelect(query)[0][0])
        mat.ajouteDatabase()
        apres = int(script.DatabaseTools.DatabaseTools().executeSelect(query)[0][0])
        self.assertEqual(avant, apres - 1)


if __name__ == '__main__':
    unittest.main()
