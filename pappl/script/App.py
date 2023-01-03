# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets, QtGui

from script import FenetreHome
from script import BandeauNavigation
from script import Projet

class App(object):
    """
    Classe principale de l'interface graphique.
    """
    def __init__(self, Frame) -> None:
        """
        Constructeur de la classe App.

        :param Frame: Une fenêtre QtFrame, dans laquelle sera créée l'interface graphique.
        """
        self.initUI(Frame)
        self.retranslateUi()

    def initUI(self, Frame) -> None:
        """
        Cette méthode va mettre en forme la fenêtre de base passée en argument du constructeur.
        Elle va également instancier les éléments suivants de l'interface :
            - La pile de fenêtres, contenant par défaut uniquement la fenêtre d'accueil.
            - Le bandeau de navigation, permettant de naviguer entre les différentes fenêtres (Accueil et fenêtres de projets).

        :param Frame: La fenêtre QtFrame passée au constructeur qui va accueillir l'interface graphique.
        """
        # Création de la fenêtre
        Frame.resize(1080, 500)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fenetre_principale = QtWidgets.QFrame(Frame)
        self.fenetre_principale.setGeometry(QtCore.QRect(0, 0, 1080, 500))
        self.fenetre_principale.setStyleSheet("background-color: rgb(224, 224, 224);color:black;")
        self.fenetre_principale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fenetre_principale.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fenetre_principale.setObjectName("fenetre_principale")

        self.pile_fenetres = QtWidgets.QStackedWidget(self.fenetre_principale)
        self.pile_fenetres.setGeometry(QtCore.QRect(0, 40, 1080, 490))
        self.pile_fenetres.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.pile_fenetres.setObjectName("pile_fenetres")

        self.frame_quickpopup = QtWidgets.QFrame(self.fenetre_principale)
        self.frame_quickpopup.setGeometry(QtCore.QRect(700, 460, 371, 31))
        self.frame_quickpopup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_quickpopup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_quickpopup.setObjectName("frame_quickpopup")
        self.frame_quickpopup.setVisible(False)

        self.label_quickpopup = QtWidgets.QLabel(self.frame_quickpopup)
        self.label_quickpopup.setGeometry(QtCore.QRect(0, 0, 371, 31))
        self.label_quickpopup.setObjectName("frame_quickpopup")
        self.label_quickpopup.setAlignment(QtCore.Qt.AlignCenter)

        self.bandeau = BandeauNavigation.BandeauNavigation(self.fenetre_principale, self)

        # Ajout fenetre HOME
        self.fenetre_home = FenetreHome.FenetreHome(self)

        # Ajout des pages à la pile
        self.pile_fenetres.addWidget(self.fenetre_home)

    def retranslateUi(self):
        """
        Méthode permettant de mettre à jour le contenu de l'interface graphique.
        Dans notre cas, uniquement la fenêtre par défaut.
        """
        _translate = QtCore.QCoreApplication.translate
        self.pile_fenetres.setCurrentIndex(0)

    def import_projet(self,
                      projet: Projet,
                      chemin_fichier: str) -> None:
        """
        Méthode permettant l'import d'un projet.

        :param projet: Le projet à importer = créer une fenêtre projet.
        :param chemin_fichier: Le chemin vers le fichier de sauvegarde.
        """
        self.bandeau.import_projet(projet, chemin_fichier)

    def quick_popup(self,
                    texte: str,
                    type: str = "Other",
                    duree: int = 10,
                    style: str = "") -> None:
        """
        Méthode permettant d'afficher un popup en bas de l'écran.
        Il est possible de passer 4 types de popup avec un style pré-définis :
            - Info : Pour indiquer une information générale
            - Error : Pour indiquer qu'une erreur a eu lieux
            - Warning : Pour indiquer qu'un événement ne s'est pas déroulé exactement comme prévu
            - Succes : Pour indiquer le bon déroulement d'une opération
        Il est possible de choisir la durée pendant laquelle le popup sera visible.

        :param texte: Le texte à inscrire dans le popup.
        :raise ValueError: Si le texte à indiquer dans le popup est vide.
        :param type: Le type de popup.
        :raise ValueError: Si le type du popup n'est pas l'un des suivants: ["Error", "Warning", "Info", "Succes", "Other"]
        :param duree: La durée durant laquelle le popup doit être visible.
        :raise ValueError: Si la durée n'est pas un entier positif ou nul.
        :param style: Le style sous forme d'une stylesheet à appliquer au popup, lors de l'utilisation d'un type "Other"
        """
        type_possible = ["Error", "Warning", "Info", "Succes", "Other"]
        if type not in type_possible:
            raise ValueError("quick_popup: type must be one of the following " + str(type_possible) + ".")
        if duree < 0:
            raise ValueError("quick_popup: duree must be a positive integer.")
        if texte.strip() == "":
            raise ValueError("quick_popup: texte cannot be empty.")
        error_stylesheet = "background-color: darkred;color:black;border-radius:5px;text-align:center;"
        warning_stylesheet = "background-color: rgb(238, 210, 2);color:black;border-radius:5px;text-align:center;"
        succes_stylesheet = "background-color: forestgreen;color:black;border-radius:5px;text-align:center;"
        info_stylesheet = "background-color: lightblue;color:black;border-radius:5px;text-align:center;"
        self.label_quickpopup.setText(texte)
        match type:
            case "Error":
                self.frame_quickpopup.setStyleSheet(error_stylesheet)
            case "Warning":
                self.frame_quickpopup.setStyleSheet(warning_stylesheet)
            case "Succes":
                self.frame_quickpopup.setStyleSheet(succes_stylesheet)
            case "Info":
                self.frame_quickpopup.setStyleSheet(info_stylesheet)
            case "Others":
                self.frame_quickpopup.setStyleSheet(style)
        self.frame_quickpopup.setVisible(True)
        self.timer = QtCore.QTimer()
        self.timer.start(duree * 1000)
        self.timer.timeout.connect(lambda: self.frame_quickpopup.setVisible(False))

def main():
    """
    Méthode permettant de créer l'interface graphique.
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    Main = App(Frame)
    Frame.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()