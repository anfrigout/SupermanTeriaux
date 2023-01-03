# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Dessin(QWidget):
    def __init__(self):
        self.__x=0
        self.__y=0
        self.__couleurTrait=Qt.darkGray
        self.__couleurRemplissage=Qt.lightGray
        self.__hauteurRect=0
        self.__largeurRect=0

    def getX(self):
        return self.__x

    def setX(self, x : int):
        self.__x=x
        
    def getY(self):
        return self.__y

    def setY(self, y : int):
        self.__x=y

    def setCouleurTrait(self, couleur : Qt):
        self.__couleurTrait=couleur

    def setCouleurRemplissage(self, couleur : Qt):
        self.__couleurRemplissage=couleur

    def getHauteurRect(self):
        return self.__hauteurRect

    def setHauteurRect(self, h : int):
        self.__hauteurRect=h
        
    def getLargeurRect(self):
        return self.__largeurRect

    def setLargeurRect(self, L : int):
        self.__largeurRect=L

    def paintEvent(self,  event):
        painter = QPainter(self) # recupere le QPainter du widget
        painter.setPen(self.__couleurTrait) # add a dark gray pen
        painter.setBrush(self.__couleurRemplissage) # set a light gray brush
        painter.drawRect(self.x,self.y,self.__hauteurRect,self.__largeurRect)