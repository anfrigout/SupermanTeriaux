from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from math import floor

from script import Plaque
from script import Projet
from script import PopupInfoPli


class FenetreDessin(QtWidgets.QWidget):
    def __init__(self, projet: Projet = None, x: int = 0 , y: int = 0,hauteurRect: int = 0, largeurRect: int = 0,
                 sourisX: int=0, sourisY: int = 0, nPli: int = 0):
        """
        Constructeur de la classe FenetreDessin
        Cette classe permet la gestion de la frame où nous affichons les différents plis de la plaque

        :param projet: Le projet associé à la page
        :param x: abscisse dans la frame qui sera utilisée pour situer ce qu'il y à à dessiner
        :param y: ordonnées dans la frame qui sera utilisée pour situer ce qu'il y à à dessiner
        :param sourisX: abscisse de la souris
        :param sourisY: ordonnée de la souris
        :param nPli: numéro du pli sélectionné avec un clic de souris
        """
        self.__x = x
        self.__y = y
        self.__hauteurRect = hauteurRect
        self.__largeurRect = largeurRect
        self.__sourisX = sourisX
        self.__sourisY = sourisY
        self.__nPli = nPli
        self.__plaque = Plaque.Plaque()
        self.__projet = projet

        super(FenetreDessin, self).__init__()
        self.popup_info_pli = PopupInfoPli.PopupInfoPli()
        self.setFixedSize(531, 341)
        self.setMouseTracking(True)
        self.show()

    def getX(self):
        """
        Getter de l'attribut x
        :return: x: int
        """
        return self.__x

    def setX(self, x: int):
        """
        setter de l'attribut x
        :param x: int
        """
        self.__x = x

    def getY(self):
        """
        Getter de l'attribut y
        :return: y: int
        """
        return self.__y

    def getPlaque(self):
        """
        Getter de l'attribut plaque
        :return: plaque: Plaque
        """
        return self.__plaque

    def setPlaque(self, p: Plaque):
        """
        setter de l'attribut plaque
        :param p: Plaque
        """
        self.__plaque = p

    def setY(self, y: int):
        """
        setter de l'attribut y
        :param y: int
        """
        self.__x = y

    def getHauteurRect(self):
        """
        Getter de l'attribut hauteurRect
        :return: hauteurRect: int
        """
        return self.__hauteurRect

    def setHauteurRect(self, h: int):
        """
        setter de l'attribut hauteurRect
        :param h: int
        """
        self.__hauteurRect = h

    def getLargeurRect(self):
        """
        Getter de l'attribut largeurRect
        :return: largeurRect: int
        """
        return self.__largeurRect

    def setLargeurRect(self, L: int):
        """
        setter de l'attribut largeurRect
        :param L: int
        """
        self.__largeurRect = L

    def getSourisX(self):
        """
        Getter de l'attribut sourisX
        :return: sourisX: int
        """
        return self.__sourisX

    def setSourisX(self, x: int):
        """
        setter de l'attribut sourisX
        :param x: int
        """
        self.__sourisX = x

    def getSourisY(self):
        """
        Getter de l'attribut sourisY
        :return: sourisY: int
        """
        return self.__sourisY

    def setX(self, y: int):
        """
        setter de l'attribut sourisY
        :param y: int
        """
        self.__sourisY = y

    def getNPli(self):
        """
        Getter de l'attribut nPli
        :return: nPli: int
        """
        return self.__nPli

    def setNPli(self, n: int):
        """
        setter de l'attribut nPli
        :param n: int
        """
        self.__nPli = n

    def getPliSelect(self):
        """
        Méthode permettant d'obtenir le pli sélectionné avec un clic de souris
        :return: plisSelect: Pli
        """
        plaqueTmp=self.__projet.getPlaque()
        nbrePli=len(plaqueTmp.getListePlis())
        if (self.__nPli>0) and (self.__nPli<=nbrePli):
            try:
                pliSelect=plaqueTmp.getListePlis()[self.__nPli-1]
                return(pliSelect)
            except ValueError:
                return None


    def mousePressEvent(self, event):
        """
        Méthode permettant de gérer le clic de souris
        Notamment à chaque clic de souris:
        Affichage d'un popup donnant les informations sur le pli sélectionné
        Remise à jour de l'affichage des plis
        """
        self.popup_info_pli.deleteLater()
        self.__sourisX = event.x()
        self.__sourisY = event.y()
        self.__nPli = floor(self.__sourisY / 20)
        self.popup_info_pli = PopupInfoPli.PopupInfoPli(self)
        self.popup_info_pli.setGeometry(QtCore.QRect(100, 100, 220, 150))
        self.popup_info_pli.setObjectName("popup_info_pli")
        self.popup_info_pli.setPos(self.__sourisX, self.__sourisY)
        self.popup_info_pli.reset_labels()
        pli=self.getPliSelect()
        if pli != None :
            try:
                self.popup_info_pli.maj_Info_Pli(pli)
                self.popup_info_pli.show()
                flag=True
            except ValueError:
                flag=False
        self.update()

    def setPos(self, x: int, y: int):
        """
        Méthode permettant de placer le popup
        :param x: abscisse de où se trouvera le popup
        :param y: ordonnées de où se trouvera le popup
        """
        x_popup=min(x, 295)
        y_popup = min(y, 190)
        self.popup_info_pli.setGeometry(QtCore.QRect(x_popup, y_popup, 220, 150))

    def drawPlis(self, painter: QPainter):
        """
        Méthode permettant l'affichage des plis dans la frame
        Notamment, le pli sélectionné est en rouge, les autres en gris
        Ils sont représentés par des rectangles
        :param painter: painter de la frame
        """
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        painter.setPen(col)
        #painter.setBrush(QColor(200, 200, 200))
        nbrePlis = len(self.__plaque.getListePlis())
        self.__y = 20
        self.__x = 10
        if nbrePlis >= 1:
            for k in range(0, nbrePlis):
                if k == self.__nPli-1:
                    painter.setBrush(QColor(200, 0, 0))
                    painter.drawRect(self.__x, self.__y, 460, 5)
                    self.__y = self.getY() + 20
                else:
                    painter.setBrush(QColor(200, 200, 200))
                    painter.drawRect(self.__x, self.__y, 460, 5)
                    self.__y = self.getY() + 20
        if nbrePlis > 13:
            new_y = 371 + (nbrePlis - 15) * 20
            self.setFixedSize(531, new_y)

    def paintEvent(self, event):
        """
        Redéfinition de la méthode paintEvent de la frame, pour pouvoir dessiner les rectangles comme définis dans la méthodes drawPlis
        """
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawPlis(painter)
        painter.end()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = FenetreDessin()
    frame_11 = QtWidgets.QScrollArea()
    frame_11.setGeometry(QtCore.QRect(310, 70, 531, 341))
    frame_11.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;")
    frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_11.setObjectName("frame_11")
    frame_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    frame_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    frame_11.setWidget(Frame)
    frame_11.show()
    sys.exit(app.exec())
