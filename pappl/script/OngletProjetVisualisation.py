# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from __future__ import annotations
from PyQt5 import QtCore, QtWidgets
from script import Canva
import numpy as np
import matplotlib.pyplot as plt


class OngletProjetVisualisation(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        Constructeur de la classe OngletProjetVisualisation
        Classe permettant la gestion/ création de l'onglet de visualisation des résultats
        :param parent: widget parent accueillant cet onglet
        """
        super(OngletProjetVisualisation, self).__init__()
        self.__parent = parent
        self.__liste_figures = [None, None, None, None, None, None]
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def getListeFigures(self) -> list:
        """
        Getter permettant d'obtenir la liste des figures pour l'export.

        :return: La liste des figures pour l'export.
        """
        return self.__liste_figures

    def generer_toutes_figures(self) -> None:
        """
        Méthode permettant de générer l'intégralité des figures et de les stocker dans __liste_figures.
        """

        def test(liste_x, liste_y, titre):
            fig, ax = plt.subplots(figsize=(5, 4), dpi=90)
            ax.plot(liste_x, liste_x)
            ax.set(title=str(titre))
            ax.grid()
            ax.set_ylim(-30, 30)
            plt.show()


        yListe = self.calcul_y()

        xListe = self.calcul_eps_l()
        if len(xListe) == len(yListe):
            self.__liste_figures[0] = test(xListe, yListe, "epsilon_l")

        xListe = self.calcul_eps_t()
        if len(xListe) == len(yListe):
            self.chart.maj_graphique(xListe, yListe, "epsilon_t")
        self.__liste_figures[1] = self.chart.getFig()

        xListe = self.calcul_gamma_lt()
        if len(xListe) == len(yListe):
            self.chart.maj_graphique(xListe, yListe, "gamma_lt")
        self.__liste_figures[2] = self.chart.getFig()

        xListe = self.calcul_sigma_l()
        if len(xListe) == len(yListe):
            self.chart.maj_graphique(xListe, yListe, "sigma_l")
        self.__liste_figures[3] = self.chart.getFig()

        xListe = self.calcul_sigma_t()
        if len(xListe) == len(yListe):
            self.chart.maj_graphique(xListe, yListe, "sigma_t")
        self.__liste_figures[4] = self.chart.getFig()

        xListe = self.calcul_to_lt()
        if len(xListe) == len(yListe):
            self.chart.maj_graphique(xListe, yListe, "tau_lt")
        self.__liste_figures[5] = self.chart.getFig()
        self.maj_label_matrices()

    def initUI(self):
        """
        Méthode pour initialiser le widget représentant l'onglet du paramétrage de la plaque
        """
        self.widget_projet_visualisation = QtWidgets.QWidget(self)
        self.widget_projet_visualisation.setObjectName("widget_projet_visualisation")

        self.frame_12 = QtWidgets.QFrame(self.widget_projet_visualisation)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 881, 421))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")

        self.label_47 = QtWidgets.QLabel(self.frame_12)
        self.label_47.setGeometry(QtCore.QRect(50, 60, 100, 16))
        self.label_47.setObjectName("label_47")

        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setGeometry(QtCore.QRect(40, 80, 350, 310))
        self.frame_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")

        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setGeometry(QtCore.QRect(410, 30, 441, 361))
        self.frame_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")

        self.label_choix_matrice = QtWidgets.QLabel(self.frame_12)
        self.label_choix_matrice.setGeometry(QtCore.QRect(50, 10, 100, 16))
        self.label_choix_matrice.setObjectName("label_choix_matrice")

        self.comboBoxMatrice = QtWidgets.QComboBox(self.frame_12)
        self.comboBoxMatrice.setGeometry(QtCore.QRect(40, 30, 231, 21))
        self.comboBoxMatrice.setObjectName("comboBoxMatrice")

        self.chart = Canva.Canva(self.frame_14, [], [], "")

        # Matrice A
        self.titre_a = QtWidgets.QLabel(self.frame_13)
        self.titre_a.setGeometry(QtCore.QRect(10, 10, 330, 15))
        self.titre_a.setObjectName("label_a")

        self.label_a = QtWidgets.QLabel(self.frame_13)
        self.label_a.setGeometry(QtCore.QRect(10, 30, 330, 52))
        self.label_a.setObjectName("label_a")

        self.titre_b = QtWidgets.QLabel(self.frame_13)
        self.titre_b.setGeometry(QtCore.QRect(10, 90, 330, 15))
        self.titre_b.setObjectName("titre_b")

        self.label_b = QtWidgets.QLabel(self.frame_13)
        self.label_b.setGeometry(QtCore.QRect(10, 110, 330, 52))
        self.label_b.setObjectName("label_b")

        self.titre_d = QtWidgets.QLabel(self.frame_13)
        self.titre_d.setGeometry(QtCore.QRect(10, 170, 330, 15))
        self.titre_d.setObjectName("titre_d")

        self.label_d = QtWidgets.QLabel(self.frame_13)
        self.label_d.setGeometry(QtCore.QRect(10, 190, 330, 52))
        self.label_d.setObjectName("label_d")

    def maj_label_matrices(self) -> None:
        """
        Méthode permettant de mettre à jour les matrices dans l'affichage.
        """
        _translate = QtCore.QCoreApplication.translate
        A = np.around(self.__parent.projet.getPlaque().getA_rigidite())
        B = np.around(self.__parent.projet.getPlaque().getB_rigidite())
        D = np.around(self.__parent.projet.getPlaque().getD_rigidite())
        a_text = "[" + str(A[0][0]) + ", " + str(A[0][1]) + ", " + str(A[0][2]) + "]\n[" + str(A[1][0]) + ", " + str(
            A[1][1]) + ", " + str(A[1][2]) + "]\n[" + str(A[2][0]) + ", " + str(A[2][1]) + ", " + str(A[2][2]) + "]"
        b_text = "[" + str(B[0][0]) + ", " + str(B[0][1]) + ", " + str(B[0][2]) + "]\n[" + str(B[1][0]) + ", " + str(
            B[1][1]) + ", " + str(B[1][2]) + "]\n[" + str(B[2][0]) + ", " + str(B[2][1]) + ", " + str(B[2][2]) + "]"
        d_text = "[" + str(D[0][0]) + ", " + str(D[0][1]) + ", " + str(D[0][2]) + "]\n[" + str(D[1][0]) + ", " + str(
            D[1][1]) + ", " + str(D[1][2]) + "]\n[" + str(D[2][0]) + ", " + str(D[2][1]) + ", " + str(D[2][2]) + "]"
        self.label_a.setText(_translate("Frame", a_text))
        self.label_b.setText(_translate("Frame", b_text))
        self.label_d.setText(_translate("Frame", d_text))

    def retranslateUi(self):
        """
        Méthode pour mettre à jour les textes à afficher sur la page
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_47.setText(_translate("Frame", "MATRICES"))
        self.label_choix_matrice.setText(_translate("Frame", "Choix du graphique :"))
        self.label_a.setText(_translate("Frame", "[NA, NA, NA]\n[NA, NA, NA]\n[NA, NA, NA]"))
        self.label_b.setText(_translate("Frame", "[NA, NA, NA]\n[NA, NA, NA]\n[NA, NA, NA]"))
        self.label_d.setText(_translate("Frame", "[NA, NA, NA]\n[NA, NA, NA]\n[NA, NA, NA]"))
        self.titre_a.setText(_translate("Frame", "Matrice A"))
        self.titre_b.setText(_translate("Frame", "Matrice B"))
        self.titre_d.setText(_translate("Frame", "Matrice D"))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def initActions(self):
        """
        Méthode permettant de connecter l'ensemble des méthodes de la page aux boutons, changement, etc..
        """
        self.remplirBox()
        self.comboBoxMatrice.currentTextChanged.connect(lambda: self.choixTrace())
        self.comboBoxMatrice.currentTextChanged.connect(lambda: self.trace())

    def trace(self):
        xListe, yListe = self.choixTrace()
        titre = self.comboBoxMatrice.currentText()
        if len(xListe) == len(yListe):
            self.chart.maj_graphique(xListe, yListe, titre)
            self.frame_14.update()

    def remplirBox(self):
        """
        Méthode permettant de remplir la comboBox qui contient les différents choix de graphique à afficher
        """
        eps_l = 'epsilon_l'
        eps_t = 'epsilon_t'
        gamma_lt = 'gamma_lt'
        sigma_l = 'sigma_l'
        sigma_t = 'sigma_t'
        to_lt = 'to_lt'
        self.comboBoxMatrice.addItems([str(eps_l), str(eps_t), str(gamma_lt), str(sigma_l), str(sigma_t), str(to_lt)])

    def choixTrace(self):
        """
        Méthode renvoyant les listes d'ordonnées/ abscisses à tracer en fonction du choix donné dans la comboBox
        """
        choix = self.comboBoxMatrice.currentText()
        xListe = []
        yListe = self.calcul_y()
        if choix == 'epsilon_l':
            xListe = self.calcul_eps_l()
            self.maj_label_matrices()
        if choix == 'epsilon_t':
            xListe = self.calcul_eps_t()
            self.maj_label_matrices()
        if choix == 'gamma_lt':
            xListe = self.calcul_gamma_lt()
            self.maj_label_matrices()
        if choix == 'sigma_l':
            xListe = self.calcul_sigma_l()
            self.maj_label_matrices()
        if choix == 'sigma_t':
            xListe = self.calcul_sigma_t()
            self.maj_label_matrices()
        if choix == 'to_lt':
            xListe = self.calcul_to_lt()
            self.maj_label_matrices()

        return xListe, yListe

    def calcul_y(self):
        """
        Méthode permettant de calculer les ordonnées du graphique
        """
        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()
        liste_y = []
        nbrePlis = len(liste_plisTmp)
        ep_total = 0
        for k in range(0, nbrePlis):
            ep_total = ep_total + liste_plisTmp[k].getEpaisseur()
        y = plaqueTmp.getZmin()
        liste_y.append(y)
        liste_y.append(y)
        for k in range(0, nbrePlis):
            y = y + liste_plisTmp[k].getEpaisseur()
            liste_y.append(y)
            liste_y.append(y)
        return liste_y

    def calcul_eps_l(self):
        """
        Méthode permettant de calculer les abscisses du graphique si le choix est epsilon_l
        """

        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()
        if len(liste_plisTmp) != 0:
            plaqueTmp.majMatrices()

        liste_y = []
        liste_x = []
        x_bas = 0
        x_haut = 0

        nbrePlis = len(liste_plisTmp)

        eps_0x, eps_0y, gamma_0xy = self.calcul_coeff_membrane()
        k_0x, k_0y, k_0xy = self.calcul_coeff_flexion()

        yListe = self.calcul_y()

        for i in range(0, 2 * nbrePlis + 1, 2):
            liste_y.append(yListe[i])

        liste_x.append(0)
        for k in range(0, nbrePlis):
            orientation = liste_plisTmp[k].getOrientation()
            y_bas = liste_y[k]
            y_haut = liste_y[k + 1]

            if orientation == 0:
                x_bas = eps_0x + k_0x * y_bas * 1000000
                x_haut = eps_0x + k_0x * y_haut * 1000000
            if orientation == 45:
                x_bas = (eps_0x + eps_0y + gamma_0xy) / 2 + (k_0x + k_0y + k_0xy) / 2 * y_bas * 1000000
                x_haut = (eps_0x + eps_0y + gamma_0xy) / 2 + (k_0x + k_0y + k_0xy) / 2 * y_haut * 1000000
            if orientation == -45:
                x_bas = (eps_0x + eps_0y - gamma_0xy) / 2 + (k_0x + k_0y - k_0xy) / 2 * y_bas * 1000000
                x_haut = (eps_0x + eps_0y - gamma_0xy) / 2 + (k_0x + k_0y - k_0xy) / 2 * y_haut * 1000000
            if orientation == 90:
                x_bas = eps_0y + k_0y * y_bas * 1000000
                x_haut = eps_0y + k_0y * y_haut * 1000000
            liste_x.append(x_bas)
            liste_x.append(x_haut)
        liste_x.append(0)
        return liste_x

    def calcul_eps_t(self):
        """
        Méthode permettant de calculer les abscisses du graphique si le choix est epsilon_t
        """

        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()

        if len(liste_plisTmp) != 0:
            plaqueTmp.majMatrices()
            plaqueTmp.majMatricesPlis()

        liste_y = []
        liste_x = []
        x_bas = 0
        x_haut = 0

        nbrePlis = len(liste_plisTmp)

        eps_0x, eps_0y, gamma_0xy = self.calcul_coeff_membrane()
        k_0x, k_0y, k_0xy = self.calcul_coeff_flexion()

        yListe = self.calcul_y()

        for i in range(0, 2 * nbrePlis + 1, 2):
            liste_y.append(yListe[i])

        liste_x.append(0)
        for k in range(0, nbrePlis):
            orientation = liste_plisTmp[k].getOrientation()
            y_bas = liste_y[k]
            y_haut = liste_y[k + 1]

            if orientation == 0:
                x_bas = eps_0y + k_0y * y_bas * 1000000
                x_haut = eps_0y + k_0y * y_haut * 1000000
            if orientation == 45:
                x_bas = (eps_0x + eps_0y - gamma_0xy) / 2 + (k_0x + k_0y - k_0xy) / 2 * y_bas * 1000000
                x_haut = (eps_0x + eps_0y - gamma_0xy) / 2 + (k_0x + k_0y - k_0xy) / 2 * y_haut * 1000000
            if orientation == -45:
                x_bas = (eps_0x + eps_0y + gamma_0xy) / 2 + (k_0x + k_0y + k_0xy) / 2 * y_bas * 1000000
                x_haut = (eps_0x + eps_0y + gamma_0xy) / 2 + (k_0x + k_0y + k_0xy) / 2 * y_haut * 1000000
            if orientation == 90:
                x_bas = eps_0x + k_0x * y_bas * 1000000
                x_haut = eps_0x + k_0x * y_haut * 1000000
            liste_x.append(x_bas)
            liste_x.append(x_haut)
        liste_x.append(0)
        return liste_x

    def calcul_gamma_lt(self):
        """
        Méthode permettant de calculer les abscisses du graphique si le choix est gamma_lt
        """

        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()

        if len(liste_plisTmp) != 0:
            plaqueTmp.majMatrices()
            plaqueTmp.majMatricesPlis()

        liste_y = []
        liste_x = []
        x_bas = 0
        x_haut = 0

        nbrePlis = len(liste_plisTmp)

        eps_0x, eps_0y, gamma_0xy = self.calcul_coeff_membrane()
        k_0x, k_0y, k_0xy = self.calcul_coeff_flexion()

        yListe = self.calcul_y()

        for i in range(0, 2 * nbrePlis + 1, 2):
            liste_y.append(yListe[i])

        liste_x.append(0)
        for k in range(0, nbrePlis):
            orientation = liste_plisTmp[k].getOrientation()
            y_bas = liste_y[k]
            y_haut = liste_y[k + 1]

            if orientation == 0:
                x_bas = gamma_0xy + k_0xy * y_bas * 1000000
                x_haut = gamma_0xy + k_0xy * y_haut * 1000000
            if orientation == 45:
                x_bas = (-eps_0x + eps_0y) + (-k_0x + k_0y) * y_bas * 1000000
                x_haut = (-eps_0x + eps_0y) + (-k_0x + k_0y) * y_haut * 1000000
            if orientation == -45:
                x_bas = (eps_0x - eps_0y) + (k_0x - k_0y) * y_bas * 1000000
                x_haut = (eps_0x - eps_0y) + (k_0x - k_0y) * y_haut * 1000000
            if orientation == 90:
                x_bas = -gamma_0xy - k_0xy * y_bas * 1000000
                x_haut = -gamma_0xy - k_0xy * y_haut * 1000000
            liste_x.append(x_bas)
            liste_x.append(x_haut)
        liste_x.append(0)
        return liste_x

    def calcul_sigma_l(self):
        """
        Méthode permettant de calculer les abscisses du graphique si le choix est sigma_l
        """
        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()

        nbrePlis = len(liste_plisTmp)

        liste_x = []
        x_bas = 0
        x_haut = 0

        v_tl = 0
        beta = 0

        liste_orientation_tmp = []
        liste_orientation_tmp.append("")
        for k in range(0, nbrePlis):
            liste_orientation_tmp.append(liste_plisTmp[k].getOrientation())
            liste_orientation_tmp.append(liste_plisTmp[k].getOrientation())
        liste_orientation_tmp.append(liste_orientation_tmp.append(liste_plisTmp[nbrePlis - 1].getOrientation()))

        liste_mat_tmp = []
        liste_mat_tmp.append(None)
        for k in range(0, nbrePlis):
            liste_mat_tmp.append(liste_plisTmp[k].getMateriau())
            liste_mat_tmp.append(liste_plisTmp[k].getMateriau())
        liste_mat_tmp.append(liste_plisTmp[nbrePlis - 1].getMateriau())

        liste_eps_l = self.calcul_eps_l()
        liste_eps_t = self.calcul_eps_t()

        longueur = len(liste_eps_l)

        for k in range(0, longueur):
            if k % 2 == 0:
                x_haut = 0
                x_bas = 0

                orientation = liste_orientation_tmp[k + 1]
                matTmp = liste_mat_tmp[k + 1]

                if orientation != "" and matTmp != None:

                    v_lt = matTmp.getV12()
                    E_l = matTmp.getE1()
                    E_t = matTmp.getE2()

                    if E_l != 0:
                        v_tl = v_lt * E_t / E_l
                    if v_lt / v_tl != 1:
                        beta = 1 / (1 - v_lt * v_tl)

                    eps_l_bas = liste_eps_l[k]
                    eps_l_haut = liste_eps_l[k + 1]
                    eps_t_bas = liste_eps_t[k]
                    eps_t_haut = liste_eps_t[k + 1]

                    x_bas = beta * (E_l * eps_l_bas + v_lt * E_t * eps_t_bas) / 1000000
                    x_haut = beta * (E_l * eps_l_haut + v_lt * E_t * eps_t_haut) / 1000000

                liste_x.append(x_bas)
                liste_x.append(x_haut)

        return liste_x

    def calcul_sigma_t(self):
        """
        Méthode permettant de calculer les abscisses du graphique si le choix est sigma_t
        """
        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()

        nbrePlis = len(liste_plisTmp)

        liste_x = []
        x_bas = 0
        x_haut = 0

        v_tl = 0
        beta = 0

        liste_orientation_tmp = []
        liste_orientation_tmp.append(liste_plisTmp[0].getOrientation())
        for k in range(0, nbrePlis):
            liste_orientation_tmp.append(liste_plisTmp[k].getOrientation())
            liste_orientation_tmp.append(liste_plisTmp[k].getOrientation())
        liste_orientation_tmp.append(liste_orientation_tmp.append(liste_plisTmp[nbrePlis - 1].getOrientation()))

        liste_mat_tmp = []
        liste_mat_tmp.append(liste_plisTmp[0].getMateriau())
        for k in range(0, nbrePlis):
            liste_mat_tmp.append(liste_plisTmp[k].getMateriau())
            liste_mat_tmp.append(liste_plisTmp[k].getMateriau())
        liste_mat_tmp.append(liste_plisTmp[nbrePlis - 1].getMateriau())

        liste_eps_l = self.calcul_eps_l()
        liste_eps_t = self.calcul_eps_t()

        longueur = len(liste_eps_l)

        liste_x.append(0)
        for k in range(1, longueur):
            if k % 2 == 0:
                x_haut = 0
                x_bas = 0

                orientation = liste_orientation_tmp[k + 1]
                matTmp = liste_mat_tmp[k + 1]

                if orientation != "" and matTmp != None:

                    v_lt = matTmp.getV12()
                    E_l = matTmp.getE1()
                    E_t = matTmp.getE2()

                    if E_l != 0:
                        v_tl = v_lt * E_t / E_l
                    if v_lt / v_tl != 1:
                        beta = 1 / (1 - v_lt * v_tl)

                    eps_l_bas = liste_eps_l[k - 1]
                    eps_l_haut = liste_eps_l[k]
                    eps_t_bas = liste_eps_t[k - 1]
                    eps_t_haut = liste_eps_t[k]

                    x_bas = beta * (E_t * eps_t_bas + v_lt * E_t * eps_l_bas) / 1000000
                    x_haut = beta * (E_t * eps_t_haut + v_lt * E_t * eps_l_haut) / 1000000

                liste_x.append(x_bas)
                liste_x.append(x_haut)
        liste_x.append(0)
        return liste_x

    def calcul_to_lt(self):
        """
        Méthode permettant de calculer les abscisses du graphique si le choix est to_lt
        """

        plaqueTmp = self.__parent.projet.getPlaque()
        liste_plisTmp = plaqueTmp.getListePlis()

        nbrePlis = len(liste_plisTmp)

        liste_x = []
        x_bas = 0
        x_haut = 0

        liste_orientation_tmp = []
        liste_orientation_tmp.append("")
        for k in range(0, nbrePlis):
            liste_orientation_tmp.append(liste_plisTmp[k].getOrientation())
            liste_orientation_tmp.append(liste_plisTmp[k].getOrientation())
        liste_orientation_tmp.append(liste_orientation_tmp.append(liste_plisTmp[nbrePlis - 1].getOrientation()))

        liste_mat_tmp = []
        liste_mat_tmp.append(None)
        for k in range(0, nbrePlis):
            liste_mat_tmp.append(liste_plisTmp[k].getMateriau())
            liste_mat_tmp.append(liste_plisTmp[k].getMateriau())
        liste_mat_tmp.append(liste_plisTmp[nbrePlis - 1].getMateriau())

        liste_gamma_lt = self.calcul_gamma_lt()

        longueur = len(liste_gamma_lt)

        for k in range(0, longueur):
            if k % 2 == 0:
                x_haut = 0
                x_bas = 0

                orientation = liste_orientation_tmp[k + 1]
                matTmp = liste_mat_tmp[k + 1]

                if orientation != "" and matTmp != None:
                    G_lt = matTmp.getG12()
                    gamma_lt_bas = liste_gamma_lt[k]
                    gamma_lt_haut = liste_gamma_lt[k + 1]

                    x_bas = G_lt * gamma_lt_bas / 1000000
                    x_haut = G_lt * gamma_lt_haut / 1000000

                liste_x.append(x_bas)
                liste_x.append(x_haut)

        return liste_x

    def calcul_coeff_membrane(self):
        """
        Méthode permettant de calculer les coefficients de membrane
        """

        eps_0x = 0
        eps_0y = 0
        gamma_0xy = 0

        Nx = 0
        Ny = 0
        Txy = 0
        Mx = 0
        My = 0
        Mxy = 0

        plaqueTmp = self.__parent.projet.getPlaque()

        A_souplesse = plaqueTmp.getA_souplesse()
        B_souplesse = plaqueTmp.getB_souplesse()

        chargement_courant = self.__parent.projet.getChargementCourant()

        if chargement_courant != None:
            Nx = chargement_courant.getNx()
            Ny = chargement_courant.getNy()
            Txy = chargement_courant.getTxy()
            Mx = chargement_courant.getMx()
            My = chargement_courant.getMy()
            Mxy = chargement_courant.getMxy()

        eps_0x = (A_souplesse[0][0] * Nx + A_souplesse[0][1] * Ny + A_souplesse[0][2] * Txy
                  + B_souplesse[0][0] * Mx + B_souplesse[0][1] * My + B_souplesse[0][2] * Mxy)

        eps_0y = (A_souplesse[1][0] * Nx + A_souplesse[1][1] * Ny + A_souplesse[1][2] * Txy
                  + B_souplesse[1][0] * Mx + B_souplesse[1][1] * My + B_souplesse[1][2] * Mxy)

        gamma_0xy = (A_souplesse[2][0] * Nx + A_souplesse[2][1] * Ny + A_souplesse[2][2] * Txy
                     + B_souplesse[2][0] * Mx + B_souplesse[2][1] * My + B_souplesse[2][2] * Mxy)

        return eps_0x, eps_0y, gamma_0xy

    def calcul_coeff_flexion(self):
        """
        Méthode permettant de calculer les coefficients de flexion
        """

        k_0x = 0
        k_0y = 0
        k_0xy = 0

        Nx = 0
        Ny = 0
        Txy = 0
        Mx = 0
        My = 0
        Mxy = 0

        plaqueTmp = self.__parent.projet.getPlaque()

        B_souplesse = plaqueTmp.getB_souplesse()
        D_souplesse = plaqueTmp.getD_souplesse()

        chargement_courant = self.__parent.projet.getChargementCourant()
        if chargement_courant != None:
            Nx = chargement_courant.getNx()
            Ny = chargement_courant.getNy()
            Txy = chargement_courant.getTxy()
            Mx = chargement_courant.getMx()
            My = chargement_courant.getMy()
            Mxy = chargement_courant.getMxy()

        k_0x = (B_souplesse[0][0] * Nx + B_souplesse[0][1] * Ny + B_souplesse[0][2] * Txy
                + D_souplesse[0][0] * Mx + D_souplesse[0][1] * My + D_souplesse[0][2] * Mxy)

        k_0y = (B_souplesse[1][0] * Nx + B_souplesse[1][1] * Ny + B_souplesse[1][2] * Txy
                + D_souplesse[1][0] * Mx + D_souplesse[1][1] * My + D_souplesse[1][2] * Mxy)

        k_0xy = (B_souplesse[2][0] * Nx + B_souplesse[2][1] * Ny + B_souplesse[2][2] * Txy
                 + D_souplesse[2][0] * Mx + D_souplesse[2][1] * My + D_souplesse[2][2] * Mxy)

        return k_0x, k_0y, k_0xy


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = OngletProjetVisualisation()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
