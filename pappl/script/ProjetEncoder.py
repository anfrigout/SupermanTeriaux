# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import json
from script import Projet


class ProjetEncoder(json.JSONEncoder):
    def default(self, projet: Projet):
        return projet.toJSON()
