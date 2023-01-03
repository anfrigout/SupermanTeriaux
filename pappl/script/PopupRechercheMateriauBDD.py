# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtGui, QtWidgets

from script import DatabaseTools
from script import Materiau


class PopupRechercheMateriauBDD(QtWidgets.QFrame):
    """
    Classe représentant le popup de recherche d'un matériau dans la base de données pour l'ajout dans les projets.
    """
    __bdd_recherche_index = None

    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe.
        """
        super(PopupRechercheMateriauBDD, self).__init__(parent)
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les composantes du popup.
            - Champ de recherche dans la base de données
            - Liste des résultats
            - Fiche du matériau selectionné dans la lisye des résultats.
        """
        self.popup = QtWidgets.QFrame(self)
        self.popup.setGeometry(QtCore.QRect(0, 0, 611, 261))
        self.popup.setStyleSheet(
            "background-color: rgba(0, 0, 0, 200);border-color: rgba(0, 0, 0, 150);border-radius: 10px;")
        self.popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup.setObjectName("popup")

        self.bouton_ajoute_selection = QtWidgets.QPushButton(self.popup)
        self.bouton_ajoute_selection.setGeometry(QtCore.QRect(10, 220, 591, 32))
        self.bouton_ajoute_selection.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);border-radius:0px")
        self.bouton_ajoute_selection.setObjectName("bouton_ajoute_selection")
        self.bouton_ajoute_selection.setFlat(False)

        self.champ_recherche = QtWidgets.QLineEdit(self.popup)
        self.champ_recherche.setGeometry(QtCore.QRect(10, 30, 591, 21))
        self.champ_recherche.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);border-style:none;border-radius:0px;border:none;")
        self.champ_recherche.setObjectName("champRechercheBDD2Projet")

        self.label = QtWidgets.QLabel(self.popup)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 16))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 200);color:rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.liste_correspondance = QtWidgets.QListView(self.popup)
        self.liste_correspondance.setGeometry(QtCore.QRect(10, 60, 211, 151))
        self.liste_correspondance.setStyleSheet(
            "background-color:rgb(255, 255, 255);color: rgb(0, 0, 0);border-radius: 0px;border:none;")
        self.liste_correspondance.setObjectName("liste_correspondance")

        self.fenetre_info = QtWidgets.QFrame(self.popup)
        self.fenetre_info.setGeometry(QtCore.QRect(230, 60, 371, 151))
        self.fenetre_info.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 0px;border:none;")
        self.fenetre_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fenetre_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fenetre_info.setObjectName("fenetre_info")

        self.label_nom = QtWidgets.QLabel(self.fenetre_info)
        self.label_nom.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_nom.setObjectName("label_nom")

        self.label_ref = QtWidgets.QLabel(self.fenetre_info)
        self.label_ref.setGeometry(QtCore.QRect(10, 30, 171, 16))
        self.label_ref.setObjectName("label_ref")

        self.label_e1 = QtWidgets.QLabel(self.fenetre_info)
        self.label_e1.setGeometry(QtCore.QRect(10, 50, 171, 16))
        self.label_e1.setObjectName("label_e1")

        self.label_e2 = QtWidgets.QLabel(self.fenetre_info)
        self.label_e2.setGeometry(QtCore.QRect(190, 50, 161, 16))
        self.label_e2.setObjectName("label_e2")

        self.label_g12 = QtWidgets.QLabel(self.fenetre_info)
        self.label_g12.setGeometry(QtCore.QRect(10, 70, 171, 16))
        self.label_g12.setObjectName("label_g12")

        self.label_v12 = QtWidgets.QLabel(self.fenetre_info)
        self.label_v12.setGeometry(QtCore.QRect(190, 70, 161, 16))
        self.label_v12.setObjectName("label_v12")

        self.label_s11c = QtWidgets.QLabel(self.fenetre_info)
        self.label_s11c.setGeometry(QtCore.QRect(10, 90, 171, 16))
        self.label_s11c.setObjectName("label_s11c")

        self.label_s22c = QtWidgets.QLabel(self.fenetre_info)
        self.label_s22c.setGeometry(QtCore.QRect(190, 90, 171, 16))
        self.label_s22c.setObjectName("label_s22c")

        self.label_s11t = QtWidgets.QLabel(self.fenetre_info)
        self.label_s11t.setGeometry(QtCore.QRect(10, 110, 171, 16))
        self.label_s11t.setObjectName("label_s11t")

        self.label_s22t = QtWidgets.QLabel(self.fenetre_info)
        self.label_s22t.setGeometry(QtCore.QRect(190, 110, 171, 16))
        self.label_s22t.setObjectName("label_s22t")

        self.label_s12 = QtWidgets.QLabel(self.fenetre_info)
        self.label_s12.setGeometry(QtCore.QRect(10, 130, 171, 16))
        self.label_s12.setObjectName("label_s12")

        self.label_fibre = QtWidgets.QLabel(self.fenetre_info)
        self.label_fibre.setGeometry(QtCore.QRect(190, 130, 171, 16))
        self.label_fibre.setObjectName("label_fibre")

        self.bouton_quitter = QtWidgets.QPushButton(self.popup)
        self.bouton_quitter.setGeometry(QtCore.QRect(585, 5, 21, 21))
        self.bouton_quitter.setStyleSheet(
            "background-color: transparent;border: none;color: white;font-size: 10px;")
        self.bouton_quitter.setObjectName("bouton_quitter")

    def quitte_popup(self) -> None:
        """
        Méthode permettant de quitter le popup.
        """
        self.deleteLater()

    def reset_labels(self) -> None:
        """
        Méthode permettant de réinitiliser le contenu des labels de la fiche du matériau selectionné.
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_nom.setText(_translate("popup", "Nom :"))
        self.label_ref.setText(_translate("popup", "Ref :"))
        self.label_e1.setText(_translate("popup", "E1 :"))
        self.label_e2.setText(_translate("popup", "E2 :"))
        self.label_g12.setText(_translate("popup", "G12 :"))
        self.label_v12.setText(_translate("popup", "v12 :"))
        self.label_s11c.setText(_translate("popup", "s11_c :"))
        self.label_s22c.setText(_translate("popup", "s22_c :"))
        self.label_s11t.setText(_translate("popup", "s11_t :"))
        self.label_s22t.setText(_translate("popup", "s22_t :"))
        self.label_s12.setText(_translate("popup", "s12 :"))
        self.label_fibre.setText(_translate("popup", "%age fibre :"))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def recherche_materiaux_bdd(self,
                                verbose: bool = True) -> list[tuple[str|float]]:
        """
        Méthode pour la recherche d'un matériau dans la base de données. La recherche s'eefectue sur les champs nom et ref de la base de données.

        :param verbose: True si les quickpopup doivent être affichés, False sinon
        :return: Les informations (nom, ref, E1, E2, G12, v12, s11c, s22c, s11t, s22t, s12 et %fibre) des matériaux correspodnant la recherche.
        """
        recherche_courante = self.champ_recherche.text().strip()
        no_result_stylesheet = "background-color: rgba(0, 0, 0, 25);color: rgb(0, 0, 0);border-radius:0px;"
        has_result_stylesheet = "background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);border-radius:0px;"
        try:
            if not recherche_courante == "":
                query = """ SELECT DISTINCT nom, reference, e1, e2, g12, v12, s11_c, s22_c, s11_t, s22_t, s12, pourcentage_fibre FROM public.materiau 
                            WHERE materiau.nom LIKE %s 
                            OR materiau.reference LIKE %s"""
                data = [str("%" + recherche_courante + "%"), str("%" + recherche_courante + "%")]
                reponses = DatabaseTools.DatabaseTools().executeSelect(query, data)

                # Ajout des resultats
                modele_liste_resultats = QtGui.QStandardItemModel()
                self.liste_correspondance.setModel(modele_liste_resultats)
                if (len(reponses)):
                    self.liste_correspondance.setStyleSheet(has_result_stylesheet)
                    self.liste_correspondance.selectionModel().currentChanged.connect(
                        self.affiche_info_selection)
                    for reponse in reponses:
                        entree = QtGui.QStandardItem(reponse[0])
                        modele_liste_resultats.appendRow(entree)
                    texte = str(len(reponses)) + " résultat(s) trouvé(s)."
                    if verbose:
                        self.quick_popup(texte, type="Info", duree=3)
                    return reponses
                else:
                    self.reset_labels()
                    self.__bdd_recherche_index = None
                    if verbose:
                        self.quick_popup("Aucun résultat...", type="Warning", duree=3)
                    self.liste_correspondance.setStyleSheet(no_result_stylesheet)
            else:
                self.reset_labels()
                self.liste_correspondance.setStyleSheet(no_result_stylesheet)
                if verbose:
                    self.quick_popup("Aucun résultat...", type="Warning", duree=3)
                self.__bdd_recherche_index = None
        except ConnectionError:
            self.reset_labels()
            self.listeBDD2Projet.setStyleSheet(no_result_stylesheet)
            if verbose:
                self.quick_popup("Impossible de se connecter à la BDD!", type="Error", duree=3)
            self.__bdd_recherche_index = None
        return []

    def affiche_info_selection(self) -> None:
        """
        Méthode pour afficher les informations du matériau selectionné dans la liste des résultats.
        """
        _translate = QtCore.QCoreApplication.translate
        index = int(self.liste_correspondance.currentIndex().row())
        self.liste_correspondance.blockSignals(True)
        if index >= 0 and not index == self.__bdd_recherche_index:
            self.__bdd_recherche_index = index
            reponses = self.recherche_materiaux_bdd(verbose=False)
            reponse_formatee = [x if x is not None else '' for x in reponses[index]]
            # Maj des champs contenant les informations à l'écran
            self.label_nom.setText(_translate("popup", "Nom : " + str(reponse_formatee[0])))
            self.label_ref.setText(_translate("popup", "Ref : " + str(reponse_formatee[1])))
            self.label_e1.setText(_translate("popup", "E1 : " + str(reponse_formatee[2])))
            self.label_e2.setText(_translate("popup", "E2 : " + str(reponse_formatee[3])))
            self.label_g12.setText(_translate("popup", "G12 : " + str(reponse_formatee[4])))
            self.label_v12.setText(_translate("popup", "v12 : " + str(reponse_formatee[5])))
            self.label_s11c.setText(_translate("popup", "s11_c : " + str(reponse_formatee[6])))
            self.label_s22c.setText(_translate("popup", "s22_c : " + str(reponse_formatee[7])))
            self.label_s11t.setText(_translate("popup", "s11_t : " + str(reponse_formatee[8])))
            self.label_s22t.setText(_translate("popup", "s22_t :" + str(reponse_formatee[9])))
            self.label_s12.setText(_translate("popup", "s12 : " + str(reponse_formatee[10])))
            self.label_fibre.setText(_translate("popup", "%age fibre : " + str(reponse_formatee[11])))

    def ajoute_selection_projet(self) -> None:
        """
        Méthode pour ajouter la matériau selectionné à la liste des matériaux du projet.
        """
        def materiau_dans_projet(mat: Materiau) -> bool:
            """
            Méthode vérifiant si le matériau selectionné est déjà présent dans le projet.

            :param mat: Le matériau à ajouter au projet.
            :return: True si le matériau n'est pas dans le projet, False s'il l'est.
            """
            i = 0
            while i < len(self.__parent.get_liste_materiaux()) and not mat.equals(self.__parent.get_liste_materiaux()[i]):
                i = i + 1
            return not i == len(self.__parent.get_liste_materiaux())

        if not self.__bdd_recherche_index is None:
            selection_database = self.recherche_materiaux_bdd()[self.__bdd_recherche_index]
            mat_a_ajouter = Materiau.Materiau(selection_database[0],
                                              selection_database[1],
                                              selection_database[2],
                                              selection_database[3],
                                              selection_database[4],
                                              selection_database[5],
                                              selection_database[6],
                                              selection_database[7],
                                              selection_database[8],
                                              selection_database[9],
                                              selection_database[10])
            if not materiau_dans_projet(mat_a_ajouter):
                self.__parent.ajoute_materiau_projet(mat_a_ajouter)
                self.__parent.affiche_materiaux_disponibles_projet()
                self.quick_popup("Matériau ajouté au projet!", type="Succes", duree=3)
            else:
                self.quick_popup("Matériau déjà dans le projet", type="Info", duree=3)
        else:
            self.quick_popup("Pas de matériau selectionné", type="Info", duree=3)

    def initActions(self) -> None:
        """
        Méthode permettant de connecter les actions au différents boutons.
        """
        self.bouton_quitter.clicked.connect(self.quitte_popup)
        self.champ_recherche.returnPressed.connect(self.recherche_materiaux_bdd)
        self.bouton_ajoute_selection.clicked.connect(self.ajoute_selection_projet)

    def retranslateUi(self) -> None:
        """
        Méthode permettant d'initialiser le contenu textuel des composants du popup
        """
        _translate = QtCore.QCoreApplication.translate
        self.bouton_ajoute_selection.setText(_translate("Frame", "AJOUTER AU PROJET"))
        self.label.setText(
            _translate("Frame", "Rechercher un matériau dans la base de données :"))
        self.label_nom.setText(_translate("popup", "Nom :"))
        self.label_ref.setText(_translate("popup", "Ref :"))
        self.label_e1.setText(_translate("popup", "E1 :"))
        self.label_e2.setText(_translate("popup", "E2 :"))
        self.label_g12.setText(_translate("popup", "G12 :"))
        self.label_v12.setText(_translate("popup", "v12 :"))
        self.label_s11c.setText(_translate("popup", "s11_c :"))
        self.label_s22c.setText(_translate("popup", "s22_c :"))
        self.label_s11t.setText(_translate("popup", "s11_t :"))
        self.label_s22t.setText(_translate("popup", "s22_t :"))
        self.label_s12.setText(_translate("popup", "s12 :"))
        self.label_fibre.setText(_translate("popup", "%age fibre :"))
        self.bouton_quitter.setText(_translate("popup", "x"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = PopupRechercheMateriauBDD()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()