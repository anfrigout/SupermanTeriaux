# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets

from script import Pli


class PopupInfoPli(QtWidgets.QFrame):
    """
    Classe représentant un popup d'info pour un pli selectionné.
    """

    def __init__(self,
                 parent=None,
                 x: int = 0,
                 y: int = 0) -> None:
        """
        Constructeur de la classe PopupInfoPli
        Classe représentant un popup donnant des informations sur le pli sélectionné avec un clic de souris
        :param parent: widget parent du popup
        :param x: abscisse du popup
        :param y: ordonnée du popup
        """
        super(PopupInfoPli, self).__init__(parent)
        self.__parent = parent
        self.__x = 0
        self.__y = 0
        self.initUI()

    def initUI(self) -> None:
        """
        Méthode pour initialiser le popup
        """
        self.popup = QtWidgets.QFrame(self)
        self.popup.setGeometry(QtCore.QRect(0, 0, 220, 150))
        self.popup.setStyleSheet(
            "background-color: rgba(0, 0, 0, 200);border-color: rgba(0, 0, 0, 150);border-radius: 10px;")
        #self.popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.popup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup.setObjectName("popup")

        self.label_titre = QtWidgets.QLabel(self.popup)
        self.label_titre.setGeometry(QtCore.QRect(60, 7, 68, 16))
        self.label_titre.setStyleSheet("background-color: rgba(0, 0, 0, 200);color:rgb(255, 255, 255);")
        self.label_titre.setObjectName("label_titre")

        self.fenetre_info = QtWidgets.QFrame(self.popup)
        self.fenetre_info.setGeometry(QtCore.QRect(10, 30, 200, 110))
        self.fenetre_info.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 0px;border:none;")
        #self.fenetre_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.fenetre_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fenetre_info.setObjectName("fenetre_info")

        self.label_materiau = QtWidgets.QLabel(self.fenetre_info)
        self.label_materiau.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label_materiau.setObjectName("label_materiau")

        self.label_orientation = QtWidgets.QLabel(self.fenetre_info)
        self.label_orientation.setGeometry(QtCore.QRect(10, 35, 161, 16))
        self.label_orientation.setObjectName("label_orientation")

        self.label_epaisseur = QtWidgets.QLabel(self.fenetre_info)
        self.label_epaisseur.setGeometry(QtCore.QRect(10, 60, 161, 16))
        self.label_epaisseur.setObjectName("label_epaisseur")

        self.label_positionRel = QtWidgets.QLabel(self.fenetre_info)
        self.label_positionRel.setGeometry(QtCore.QRect(10, 85, 161, 16))
        self.label_positionRel.setObjectName("label_positionRel")

    def reset_labels(self) -> None:
        """
        Méthode permettant de réinitialiser les champs du popup
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_titre.setText(_translate("popup", "INFO PLI"))
        self.label_materiau.setText(_translate("popup", "Matériau : "))
        self.label_orientation.setText(_translate("popup", "Orientation (°): "))
        self.label_epaisseur.setText(_translate("popup", "Epaisseur : "))
        self.label_positionRel.setText(_translate("popup", "Position relative :"))

    def maj_Info_Pli(self,
                     pli: Pli) -> None:
        """
        Méthode mettant à jour les informations concernant le pli sélectionné

        :param pli: pli sélectionné et dont les informations vont être affichés
        """
        _translate = QtCore.QCoreApplication.translate
        mat = pli.getMateriau().getNom()
        o = pli.getOrientation()
        e = pli.getEpaisseur()
        pos = pli.getPositionRelPlaque()
        self.label_materiau.setText(_translate("popup", "Matériau : " + str(mat)))
        self.label_epaisseur.setText(_translate("popup", "Epaisseur : " + str(e)))
        self.label_orientation.setText(_translate("popup", "Orientation (°): " + str(o)))
        self.label_positionRel.setText(_translate("popup", "Position relative : " + str(pos)))

    def getPos(self) -> tuple[int, int]:
        """
        Getter permettant d'obtenir la position du popup

        :return: x, y: position du clique
        """
        return self.__x, self.__y

    def setPos(self,
               x: int,
               y: int) -> None:
        """
        Méthode permettant de mettre à jour la position du popup
        """
        self.__parent.setPos(x, y)
        self.__x = x
        self.__y = y


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = PopupInfoPli()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
