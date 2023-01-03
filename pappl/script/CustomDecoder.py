# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import json
from script import Projet
from script import Plaque
from script import Pli
from script import Materiau
from script import Chargement


class CustomDecoder(json.JSONDecoder):
    """
    Decoder personnalisé pour extraire le contenu d'un fichier JSON.
    Les classes suivantes sont prises en charge par le decoder :
        - Projet
        - Plaque
        - Pli
        - Chargement
        - Materiau
    """

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        try:
            if "__type__" in dct and dct['__type__'] == "Projet":
                projet = Projet.Projet(dct['nom_projet'],
                                       dct['liste_materiaux'],
                                       dct['chargement_courant'],
                                       dct['liste_chargements'],
                                       dct['plaque'],
                                       dct['n_pli_ajout'],
                                       dct['pli_aj'])
                return projet
            if "__type__" in dct and dct["__type__"] == "Plaque":
                plaque = Plaque.Plaque(list(dct['listePlis']), dct['zmin'])
                try:
                    plaque.majMatrices()
                except: pass
                return plaque
            if "__type__" in dct and dct["__type__"] == "Pli":
                pli = Pli.Pli(float(dct['orientation']),
                              dct['materiau'],
                              float(dct['epaisseur']),
                              int(dct['positionRelPlaque']))
                pli.majMatrices()
                return pli
            if "__type__" in dct and dct['__type__'] == "Materiau":
                return Materiau.Materiau(dct['nom'],
                                         dct['ref'],
                                         float(dct['E1']),
                                         float(dct['E2']),
                                         float(dct['G12']),
                                         float(dct['v12']),
                                         float(dct['s11c']),
                                         float(dct['s22c']),
                                         float(dct['s11t']),
                                         float(dct['s22t']),
                                         float(dct['s12']),
                                         float(dct['pourcentage_fibre']))
            if "__type__" in dct and dct['__type__'] == "Chargement":
                return Chargement.Chargement(dct['nom'],
                                             float(dct['nx']),
                                             float(dct['ny']),
                                             float(dct['txy']),
                                             float(dct['mx']),
                                             float(dct['my']),
                                             float(dct['mxy']))
        except:
            raise KeyError("Fichier corrompu!")