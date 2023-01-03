# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets

from script import FenetreProjet
from script import Projet


class BandeauNavigation(QtWidgets.QWidget):
    """
    Classe représentant le bandeau de navigation principal entre la fenêtre d'accueil et les différentes fenêtres de projets.
    Pour le moment, il n'est pas possible d'ouvir plus de 8 projets en même temps.
    """
    __taille_onglet = 115 # taille d'un onglet dans le bandeau
    __liste_projets = list() # La liste de l'ensemble des projets ouverts
    __liste_onglets = list() # La liste de l'ensemble des onglets, permettant de naviguer entre les différents projets
    __liste_fermeture = list() # Boutons pour fermer les onglets
    # Style pour les onglets
    __onglet_selectionne_stylesheet = "background-color: rgb(53, 53, 53);border:none;color: rgb(255, 255, 255);"
    __onglet_non_selectionne_stylesheet = "background-color: rgb(85, 85, 85);border:none;color: rgb(255, 255, 255);"
    __fermer_onglet_non_selectionne_stylesheet = """QPushButton {
                                                        background-color: rgb(85, 85, 85);
                                                        border:none;
                                                        color: rgb(85, 85, 85);
                                                    }
                                                    QPushButton::hover {
                                                        color:white
                                                    }"""
    __fermer_onglet_selectionne_stylesheet = """QPushButton {
                                                            background-color: rgb(53, 53, 53);
                                                            border:none;
                                                            color: white;
                                                        }"""

    def __init__(self,
                 parent=None,
                 app=None) -> None:
        """
        Constructeur de la classe BandeauNavigation.
        :param parent: Un objet Qt qui recevra le Widget BandeauNavigation.
        :param app: L'objet contenant l'application globale.
        """
        super(BandeauNavigation, self).__init__(parent)
        self.__parent = parent
        self.__app = app
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser le contenu du bandeau de navigation.
        Par défaut, les éléments suivants sont ajoutés et mis en forme :
            - Le bandeau recevant les onglets
            - Un onglet pour la page d'accueil
            - Un bouton pour ajouter des onglets projets
        """
        self.bandeau = QtWidgets.QFrame(self)
        self.bandeau.setGeometry(QtCore.QRect(0, 0, 1080, 40))
        self.bandeau.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bandeau.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandeau.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bandeau.setObjectName("bandeau")

        # Bouton HOME
        self.bouton_home = QtWidgets.QPushButton(self.bandeau)
        self.bouton_home.setGeometry(QtCore.QRect(0, 0, self.__taille_onglet, 40))
        self.bouton_home.setStyleSheet(self.__onglet_selectionne_stylesheet)
        self.bouton_home.setObjectName("bouton_home")
        self.bouton_home.setFlat(False)

        # Prévision d'une version avec plus de 8 projets maximum
        self.bandeau_dynamique = QtWidgets.QFrame(self.bandeau)
        self.bandeau_dynamique.setGeometry(QtCore.QRect(self.__taille_onglet, 0, 1080-self.__taille_onglet, 40))
        self.bandeau_dynamique.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bandeau_dynamique.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandeau_dynamique.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bandeau_dynamique.setObjectName("bandeau_dynamique")

        # Bouton ajouter PROJET
        self.bouton_ajouter_projet = QtWidgets.QPushButton(self.bandeau_dynamique)
        self.bouton_ajouter_projet.setGeometry(QtCore.QRect(0, 0, 20, 40))
        self.bouton_ajouter_projet.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);border:none;")
        self.bouton_ajouter_projet.setObjectName("bouton_ajouter_projet")
        self.bouton_ajouter_projet.setFlat(False)

    def retranslateUi(self) -> None:
        """
        Cette méthode permet de mettre à jour le contenu (ici textuel) dans composant du bandeau de navigation.
        """
        _translate = QtCore.QCoreApplication.translate
        self.bouton_home.setText(_translate("bandeau", "HOME"))
        self.bouton_ajouter_projet.setText(_translate("bandeau", "+"))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__app is None:
            self.__app.quick_popup(*args, **kwargs)

    def aller_home(self) -> None:
        """
        Méthode permettant de se rendre sur la fenêtre d'accueil de l'application.
        Cette méthode va changer le style des onglets pour les mettres en non selectionné sauf l'onglet correspondant à la page d'accuei.
        """
        self.bouton_home.setStyleSheet(self.__onglet_selectionne_stylesheet)
        self.__app.pile_fenetres.setCurrentIndex(0)
        for i in range(0, len(self.__liste_onglets)):
            self.__liste_onglets[i].setStyleSheet(self.__onglet_non_selectionne_stylesheet)
            self.__liste_fermeture[i].setStyleSheet(self.__fermer_onglet_non_selectionne_stylesheet)

    def maj_nom_onglet(self):
        """
        Cette méthode permet de mettre à jour le nom d'un onglet lors du changement de nom d'un projet.
        """
        for i in range(0, len(self.__liste_onglets)):
            self.__liste_onglets[i].setText(QtCore.QCoreApplication.translate("Frame", self.__liste_projets[i].projet.getNomProjet()))

    def import_projet(self,
                      projet: Projet,
                      chemin: str) -> None:
        """
        Méthode utiliser pour l'import d'un projet.
        Si le projet est déjà ouvert alors l'import est annulé et la fenêtre change pour celle du projet.

        :param projet: Le projet à importer.
        :param chemin: Le chemin vers le fichier de sauvegarde.
        """
        index_projet = len(self.__liste_projets) + 1
        if index_projet < 8:
            # Vérification que le projet n'est pas déjà ouvert
            if True in [fenetre_projet.getCheminFichierSauvegarde() == chemin for fenetre_projet in self.__liste_projets]:
                self.quick_popup("Le projet est déjà ouvert!")
                self.aller_projet([fenetre_projet.getCheminFichierSauvegarde() == chemin for fenetre_projet in self.__liste_projets].index(True))
                return
            debut_position_bandeau = self.__taille_onglet*(index_projet-1)
            self.bouton_projet = QtWidgets.QPushButton(self.bandeau_dynamique)
            self.bouton_projet.setGeometry(QtCore.QRect(debut_position_bandeau, 0, self.__taille_onglet, 40))
            self.bouton_projet.setStyleSheet(self.__onglet_non_selectionne_stylesheet)
            self.bouton_projet.setObjectName("bouton_projet")
            self.bouton_projet.setFlat(False)

            # Fermeture de l'onglet
            self.bouton_fermer_projet = QtWidgets.QPushButton(self.bandeau_dynamique)
            self.bouton_fermer_projet.setGeometry(
                QtCore.QRect(debut_position_bandeau + self.__taille_onglet, 0, 15, 40))
            self.bouton_fermer_projet.setStyleSheet(self.__fermer_onglet_selectionne_stylesheet)
            self.bouton_fermer_projet.setObjectName("bouton_fermer_projet")
            self.bouton_fermer_projet.show()
            self.__liste_fermeture.append(self.bouton_fermer_projet)
            self.bouton_fermer_projet.clicked.connect(lambda: self.fermer_projet(index_projet - 1))

            # Creation d'une fenetre projet associée
            self.fenetre_projet = FenetreProjet.FenetreProjet(self, self.__app)
            self.fenetre_projet.setObjectName("fenetre_projet")
            self.fenetre_projet.projet = projet
            self.fenetre_projet.maj_provenance(chemin)

            # Mise à jour des pages
            self.fenetre_projet.widget_materiaux.affiche_materiaux_disponibles_projet()
            self.fenetre_projet.widget_plaque.affichePlaque()
            self.fenetre_projet.widget_chargement.maj_page_chargement()

            # Ajout du projet dans la liste des projets
            self.__liste_projets.append(self.fenetre_projet)
            # Ajout à la pile de fenêtre
            self.__app.pile_fenetres.addWidget(self.fenetre_projet)
            # Déplacement du bouton +
            self.bouton_ajouter_projet.setGeometry(QtCore.QRect((len(self.__liste_projets))* self.__taille_onglet+15, 0, 20, 40))
            # Ajout d'une fonction pour le deplacement entre les projets
            self.bouton_projet.clicked.connect(lambda: self.aller_projet(index_projet - 1))
            self.quick_popup("Projet importé!", type="Succes", duree=3)
            self.bouton_projet.show()
            self.__liste_onglets.append(self.bouton_projet)
            # Déplacement vers le nouveau projet
            self.aller_projet(index_projet - 1)
            self.bouton_projet.setText(
                QtCore.QCoreApplication.translate("Frame", self.fenetre_projet.projet.getNomProjet()))
            self.bouton_fermer_projet.setText(QtCore.QCoreApplication.translate("Frame", "x"))

        else:
            self.__app.quick_popup("Nombre maximal de projet atteint!", type="Error", duree=3)

    def ajoute_projet(self) -> None:
        """
        Cette méthode permet de créer un nouveau projet, dans la limite de 8 projets maximum.
        Par défaut le nom projet sera appelé PROJET et sera complètement vide.
        Si le nombre de projet maximal est atteint, un popup de type Error, s'affiche en bas de l'écran.
        """
        index_projet = len(self.__liste_projets) + 1
        if index_projet < 8:
            debut_position_bandeau = self.__taille_onglet*(index_projet-1)
            # Creation de l'onglet
            self.bouton_projet = QtWidgets.QPushButton(self.bandeau_dynamique)
            self.bouton_projet.setGeometry(QtCore.QRect(debut_position_bandeau, 0, self.__taille_onglet - 15, 40))
            self.bouton_projet.setStyleSheet(self.__onglet_non_selectionne_stylesheet)
            self.bouton_projet.setObjectName("bouton_projet")
            self.bouton_projet.setFlat(False)

            # Fermeture de l'onglet
            self.bouton_fermer_projet = QtWidgets.QPushButton(self.bandeau_dynamique)
            self.bouton_fermer_projet.setGeometry(QtCore.QRect(debut_position_bandeau+self.__taille_onglet-15, 0, 15, 40))
            self.bouton_fermer_projet.setStyleSheet(self.__fermer_onglet_selectionne_stylesheet)
            self.bouton_fermer_projet.setObjectName("bouton_fermer_projet")
            self.bouton_fermer_projet.show()
            self.__liste_fermeture.append(self.bouton_fermer_projet)
            self.bouton_fermer_projet.clicked.connect(lambda : self.fermer_projet(index_projet-1))

            # Creation d'une fenetre projet associée
            self.fenetre_projet = FenetreProjet.FenetreProjet(self, self.__app)
            self.fenetre_projet.setObjectName("fenetre_projet")

            # Ajout du projet dans la liste des projets
            self.__liste_projets.append(self.fenetre_projet)
            # Ajout à la pile de fenêtre
            self.__app.pile_fenetres.addWidget(self.fenetre_projet)
            # Déplacement du bouton +
            self.bouton_ajouter_projet.setGeometry(QtCore.QRect(debut_position_bandeau+self.__taille_onglet, 0, 20, 40))
            # Ajout d'une fonction pour le deplacement entre les projets
            self.bouton_projet.clicked.connect(lambda: self.aller_projet(index_projet-1))
            self.bouton_projet.show()
            self.__liste_onglets.append(self.bouton_projet)
            # Déplacement vers le nouveau projet
            self.aller_projet(index_projet-1)
            self.bouton_projet.setText(QtCore.QCoreApplication.translate("Frame", self.fenetre_projet.projet.getNomProjet()))
            self.bouton_fermer_projet.setText(QtCore.QCoreApplication.translate("Frame", "x"))
        else:
            self.__app.quick_popup("Impossible de créer plus de 8 projets", type="Error", duree=3)

    def fermer_projet(self,
                      index: int) -> None:
        """
        Classe permettant de fermer un projet.

        :param index: Index du projet dans la liste des projets.
        """
        self.aller_projet(index)
        if self.__liste_projets[index].demande_fermer_projet(index):
            # On vide la pile de fenêtre
            for projet in self.__liste_projets:
                self.__app.pile_fenetres.removeWidget(projet)
            # On supprime ce qui n'est plus util
            ancienne_fenetre = self.__liste_projets[index] # Fenetre projet
            ancienne_fenetre.deleteLater()
            self.__liste_projets.pop(index)
            ancien_bouton = self.__liste_onglets[index] # Bouton projet
            self.__liste_onglets.pop(index)
            ancien_bouton.deleteLater()
            ancien_bouton_fermer = self.__liste_fermeture[index] # Bouton fermer
            self.__liste_fermeture.pop(index)
            ancien_bouton_fermer.deleteLater()

            # On met à jour les actions
            for i in range(0, len(self.__liste_projets)):
                self.__app.pile_fenetres.insertWidget(i+1, self.__liste_projets[i])
                self.__liste_onglets[i].clicked.disconnect()
                self.__liste_fermeture[i].clicked.disconnect()
                # On deplace les onglets
                self.__liste_onglets[i].setGeometry(QtCore.QRect(i*self.__taille_onglet, 0, self.__taille_onglet-15, 40))
                self.__liste_fermeture[i].setGeometry(QtCore.QRect((i+1)*self.__taille_onglet-15, 0, 15, 40))

            self.reconnecte_onglet()

            # On replace le bouton ajouter projet
            self.maj_nom_onglet()
            self.bouton_ajouter_projet.setGeometry(QtCore.QRect(len(self.__liste_onglets)*self.__taille_onglet, 0, 20, 40))
            self.aller_home()

    def reconnecte_onglet(self) -> None:
        """
        Méthode pour reconnecter les onglets à la navigation et éviter les effets de bord des fonction lambda.
        """
        for i in range(0, len(self.__liste_projets)):
            self.connecte_onglet(i)
            self.connecte_fermeture(i)

    def connecte_onglet(self,
                        index: int) -> None:
        """
        Méthode pour reconnecter les onglets (choix des projets) à la navigation et éviter les effets de bord des fonction lambda.
        """
        self.__liste_onglets[index].clicked.connect(lambda: self.aller_projet(index))

    def connecte_fermeture(self,
                           index: int) -> None:
        """
        Méthode pour reconnecter les onglets (fermeture des projets) à la navigation et éviter les effets de bord des fonction lambda.
        """
        self.__liste_fermeture[index].clicked.connect(lambda: self.fermer_projet(index))

    def aller_projet(self,
                     index: int) -> None:
        """
        Méthode permettant de se rendre sur l'onglet d'un projet précis.
        Attention : cette méthode n'est jamais utilisée directement, elle est connéctée comme action à effectuer lors de la selection d'un onglet.
        :param index: index du projet dans la liste des projets en cours d'utilisation
        """
        self.__app.pile_fenetres.setCurrentIndex(index+1)
        self.bouton_home.setStyleSheet(self.__onglet_non_selectionne_stylesheet)
        # Mise à jour des couleurs des onglets
        for i in range(0, len(self.__liste_onglets)):
            if i == index:
                self.__liste_onglets[i].setStyleSheet(self.__onglet_selectionne_stylesheet)
                self.__liste_fermeture[i].setStyleSheet(self.__fermer_onglet_selectionne_stylesheet)
            else:
                self.__liste_onglets[i].setStyleSheet(self.__onglet_non_selectionne_stylesheet)
                self.__liste_fermeture[i].setStyleSheet(self.__fermer_onglet_non_selectionne_stylesheet)

    def initActions(self):
        """
        Méthode permettant de connecter les actions nécessaires au fonctionnement de l'application
        """
        self.bouton_home.clicked.connect(self.aller_home)
        self.bouton_ajouter_projet.clicked.connect(self.ajoute_projet)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = BandeauNavigation()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
