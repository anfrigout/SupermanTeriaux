# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import json
from script import Pli


class PliEncoder(json.JSONEncoder):
    """
    Encoder personnalisé pour les objets de la classe Pli.
    """
    def default(self, pli: Pli):
        return pli.toJSON()
