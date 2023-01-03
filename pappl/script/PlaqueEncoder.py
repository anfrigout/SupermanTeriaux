# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import json
from script import Plaque


class PlaqueEncoder(json.JSONEncoder):
    """
    Encoder personnalisé pour les objets de la classe Plaque.
    """
    def default(self,
                plaque: Plaque):
        return plaque.toJSON()
