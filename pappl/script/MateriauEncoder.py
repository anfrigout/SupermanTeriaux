# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import json
from script import Materiau


class MateriauEncoder(json.JSONEncoder):
    """
    Encoder personnalisé pour les objets de la classe Materiau.
    """
    def default(self, mat: Materiau):
        return mat.toJSON()

