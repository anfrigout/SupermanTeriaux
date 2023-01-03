# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import json
from script import Chargement


class ChargementEncoder(json.JSONEncoder):
    """
    Encoder personnalisé pour les objets de la classe Chargement.
    """
    def default(self, chargement: Chargement):
        return chargement.toJSON()
