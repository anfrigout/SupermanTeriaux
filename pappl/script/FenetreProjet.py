# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import sys
import os
from PyQt5 import QtCore, QtWidgets, QtGui
import json
import matplotlib.pyplot as plt

from script import NavigationProjet
from script import Projet
from script import OngletProjetMateriaux
from script import OngletProjetPlaque
from script import OngletProjetChargement
from script import PopupRenommageProjet
from script import BandeauProjet
from script import ProjetEncoder
from script import PopupProjetNonSauvegarde
from script import OngletProjetVisualisation


class FenetreProjet(QtWidgets.QWidget):
    """
    Méthode représentant une fenêtre pour la gestion d'un projet.
    """
    projet = None
    bdd_recherche_index = None
    __is_saved = False
    __fichier_save = None

    def __init__(self,
                 parent=None,
                 app=None) -> None:
        """
        Constructeur de la classe fenêtre projet.
        Par défautnun nouveau projet sera créé.
        Dans le cadre de l'import d'un projet, le projet associé à la fenêtre sera un clone du projet obtenu depuis le fichier de sauvegarde.
        :param parent: Un objet Qt qui recevra le Widget FenetreProjet.
        """
        super(FenetreProjet, self).__init__()
        self.__parent = parent
        self.__app = app
        self.projet = Projet.Projet("PROJET")
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def getCheminFichierSauvegarde(self) -> str:
        """
        Getter permettant d'obtenir le chemin vers le fichier de sauvegarde.

        :return: Le chemin vers le fichier de sauvegarde.
        """
        return self.__fichier_save

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser le contenu de la fenêtre projet.
        """
        # Navigation latérale
        self.navigation = NavigationProjet.NavigationProjet(self)
        self.navigation.setObjectName("navigation")

        # Bandeau supérieur
        self.bandeau = BandeauProjet.BandeauProjet(self)

        # Contenu de la page
        self.pile_onglets = QtWidgets.QStackedWidget(self)
        self.pile_onglets.setGeometry(QtCore.QRect(200, 40, 881, 421))
        self.pile_onglets.setObjectName("pile_onglets")

        self.widget_materiaux = OngletProjetMateriaux.OngletProjetMateriaux(self)
        self.widget_plaque = OngletProjetPlaque.OngletProjetPlaque(self)
        self.widget_chargement = OngletProjetChargement.OngletprojetChargement(self)
        self.widget_visualisation = OngletProjetVisualisation.OngletProjetVisualisation(self)

        # Ajout des pages à la pile
        self.pile_onglets.addWidget(self.widget_materiaux)
        self.pile_onglets.addWidget(self.widget_plaque)
        self.pile_onglets.addWidget(self.widget_chargement)
        self.pile_onglets.addWidget(self.widget_visualisation)

    def retranslateUi(self) -> None:
        """
        Méthode permettant d'initialiser le contenu de la fenêtre projet (position dans la pile d'onglet, contenu textuel...)
        """
        _translate = QtCore.QCoreApplication.translate
        self.pile_onglets.setCurrentIndex(0)
        self.navigation.bouton_materiaux.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")

    def maj_provenance(self,
                       chemin: str) -> None:
        """
        Méthode pour mettre à jour le chemin vers le fichier de sauvegarde du projet.
        Cette méthode est utilisée lors d'un import de projet.

        :param chemin: Le chemin vers le fichier de sauvegarde utilisé pour restaurer le projet.
        """
        self.__fichier_save = chemin
        self.__is_saved = True

    def aller_materiaux(self) -> None:
        """
        Méthode permettant d'aller dans l'onglet gestion des matériaux du projet.
        Cette méthode est associée à l'onglet "Gestion Matériaux" de la navigation
        """
        self.pile_onglets.setCurrentIndex(0)
        self.navigation.bouton_materiaux.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")
        self.navigation.bouton_plaque.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_chargement.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_visualisation.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

    def aller_plaque(self):
        """
        Méthode permettant d'aller dans l'onglet gestion de la plaque du projet.
        Cette méthode est associée à l'onglet "Paramètrage Plaque" de la navigation
        """
        self.pile_onglets.setCurrentIndex(1)
        self.widget_plaque.comboBox_Materiaux_Plaque()
        self.navigation.bouton_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_chargement.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_plaque.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")
        self.navigation.bouton_visualisation.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

    def aller_chargement(self):
        """
        Méthode permettant d'aller dans l'onglet gestion des chargements du projet.
        Cette méthode est associée à l'onglet "Chargement" de la navigation
        """
        self.pile_onglets.setCurrentIndex(2)
        self.navigation.bouton_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_plaque.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_chargement.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")
        self.navigation.bouton_visualisation.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

    def aller_visualisation(self):
        """
        Méthode permettant d'aller dans l'onglet visualisation du projet.
        Cette méthode est associée à l'onglet "Visualisation" de la navigation"
        """
        self.pile_onglets.setCurrentIndex(3)
        self.navigation.bouton_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_plaque.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_chargement.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_visualisation.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")

    def change_nom_projet(self) -> None:
        """
        Méthode permettant de changer le nom d'un projet.
        Cette méthode va ouvrir un popup pour effectuer cette action.
        """
        self.popup_change_nom_projet = PopupRenommageProjet.PopupRenommageProjet(self)
        self.popup_change_nom_projet.setGeometry(QtCore.QRect(10, 45, 300, 100))
        self.popup_change_nom_projet.setObjectName("popup_change_nom_projet")
        self.popup_change_nom_projet.show()

    def save(self) -> bool:
        """
        Méthode pour sauvegarder le contenu d'un projet dans un fichier au format JSON.
        """
        if self.__is_saved:
            self.quick_popup("Pas de modifications à enregistrer!", type="Info", duree=3)
            return True
        else:
            if self.__fichier_save is None or not os.path.isfile(self.__fichier_save):
                self.save_as()
            else:
                projet_json = json.dumps(self.projet, cls=ProjetEncoder.ProjetEncoder, indent=4)
                fichier = open(self.__fichier_save, "w")
                fichier.write(projet_json)
                fichier.close()
                self.quick_popup("Projet enregistré!", type="Succes", duree=3)
                self.__is_saved = True
                return True

    def save_as(self) -> bool:
        """
        Méthode pour sauvegarder le contenu d'un projet dans un fichier au format JSON, en précisant le chemin du fichier.

        :param chemin: Le chemin du fichier au sauvegarder le projet.
        """
        if self.__is_saved:
            self.quick_popup("Pas de modification à enregistrer!", type="Info", duree=3)
            return True
        try:
            projet_json = json.dumps(self.projet, cls=ProjetEncoder.ProjetEncoder, indent=4)
            options = QtWidgets.QFileDialog.Options()
            if sys.platform == 'darwin':
                options |= QtWidgets.QFileDialog.DontUseNativeDialog
            self.__fichier_save = QtWidgets.QFileDialog.getSaveFileName(self, caption='Save As',
                                                                        directory=QtCore.QDir.currentPath(),
                                                                        filter='JSON (*.json*)',
                                                                        options=options)[0]
            if not str(self.__fichier_save).endswith(".json"):
                self.__fichier_save = str(self.__fichier_save) + ".json"
            fichier = open(self.__fichier_save, "w")
            fichier.write(projet_json)
            fichier.close()
            self.quick_popup("Projet enregistré!", type="Succes", duree=3)
            self.__is_saved = True
            return True
        except:
            self.quick_popup("Erreur lors de la sauvegarde!", type="Error", duree=5)
            return False

    def demande_fermer_projet(self, index) -> bool:
        if self.__is_saved:
            return True
        else:
            self.popup_fermer_projet_non_sauvegarder = PopupProjetNonSauvegarde.PopupProjetNonSauvegarde(self, index)
            self.popup_fermer_projet_non_sauvegarder.setVisible(True)

    def quitte_popup_annuler(self) -> bool:
        self.popup_fermer_projet_non_sauvegarder.setVisible(False)
        return False

    def quitte_popup_save(self, index) -> bool:
        self.popup_fermer_projet_non_sauvegarder.setVisible(False)
        self.save()
        self.__app.bandeau.fermer_projet(index)

    def quitte_popup_no_save(self, index) -> bool:
        self.popup_fermer_projet_non_sauvegarder.setVisible(False)
        self.__is_saved = True
        self.__app.bandeau.fermer_projet(index)

    def export_visualisation(self) -> None:
        if None in self.widget_visualisation.getListeFigures():
            self.quick_popup("Résolution non effectuée, export impossible...", type="Error", duree=3)
        else:
            liste_figures = self.widget_visualisation.getListeFigures()
            fig, axs = plt.subplots(2, 3)
            axs[0][0] = liste_figures[0]
            axs[0][1] = liste_figures[1]
            axs[0][2] = liste_figures[2]

            axs[1][0] = liste_figures[3]
            axs[1][1] = liste_figures[4]
            axs[1][2] = liste_figures[5]
            fig.tight_layout()
            plt.subplots_adjust(top=0.9)
            fig.suptitle("Figures PROJET : " + self.projet.getNomProjet())

            options = QtWidgets.QFileDialog.Options()
            if sys.platform == 'darwin':
                options |= QtWidgets.QFileDialog.DontUseNativeDialog
            chemin_export = QtWidgets.QFileDialog.getSaveFileName(self, caption='Save As',
                                                                        directory=QtCore.QDir.currentPath(),
                                                                        filter='PDF (*.pdf*)',
                                                                        options=options)[0]

            if str(chemin_export).strip().startswith(".") or str(chemin_export).strip() == "":
                self.quick_popup("Nom incorrect!", type="Error", duree=3)
                return
            if not str(chemin_export).endswith(".pdf"):
                chemin_export = chemin_export + ".pdf"
            try:
                plt.savefig(chemin_export, orientation='landscape')
                self.quick_popup("Enregistrement effectué!", type="Succes", duree=3)
            except:
                self.quick_popup("Erreur lors de l'export des visualisation!", type="Error", duree=3)

    def initActions(self) -> None:
        """
        Méthode permettant de connecter les actions pour permettre la navigation et le fonctionnement de l'interface.
        """
        self.navigation.bouton_materiaux.clicked.connect(self.aller_materiaux)
        self.navigation.bouton_plaque.clicked.connect(self.aller_plaque)
        self.navigation.bouton_chargement.clicked.connect(self.aller_chargement)
        self.navigation.bouton_visualisation.clicked.connect(self.aller_visualisation)
        self.navigation.bouton_export_visualisation.clicked.connect(self.export_visualisation)
        self.bandeau.bouton_renommer.clicked.connect(self.change_nom_projet)
        self.bandeau.bouton_save.clicked.connect(self.save)
        self.bandeau.bouton_save_as.clicked.connect(self.save_as)
        self.bandeau.bouton_resoudre.clicked.connect(self.widget_visualisation.generer_toutes_figures)

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def setNomProjet(self, nom: str) -> None:
        """
        Méthode permettant de mettre à jour le nom du projet courant et de demander à l'instance parente de changer le nom de l'onglet.
        :param nom: Le nouveau nom du projet.
        """
        self.projet.setNomProjet(nom)
        self.__parent.maj_nom_onglet()

    def modification_effectuee(self) -> None:
        """
        Méthode utilisée par les instances filles pour informer que le projet a été modifée, afin de permettre de demander la sauvegarde uniquement si nécessaire.
        """
        self.__is_saved = False


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = FenetreProjet()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
