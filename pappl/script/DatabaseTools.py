# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1
import json
import psycopg2


class DatabaseTools:
    """
    Cette classe est une boite noire pour la gestion de la base de données.
    """

    def __init__(self):
        """
        Constructeur d'initialisation de la classe DatabaseTools.
        """
        self.__config=None
        self.__conn=None
        self.__cursor=None

    def __chargeConfig(self) -> None:
        """
        Méthode permettant de récupérer les informations de connexion présentes dans le fichier de configuration `/conf/.database.proprieties`.
        """
        with open('../conf/.database.proprieties') as f:
            self.__config = json.load(f)

    def __connect(self) -> None:
        """
        Méthode permettant d'initialiser la connexion à la base de données à partir des informations de connexion.

        :raise ConnectionError: Lors de l'échec de la connexion à la base de données.
        """
        self.__chargeConfig()
        self.__conn=None
        try:
            self.__conn=psycopg2.connect(
                dbname=self.__config.get('db_name'),
                host=self.__config.get('host_name'),
                user=self.__config.get('username'),
                password=self.__config.get('password')
            )
            self.__cursor=self.__conn.cursor()
        except:
            self.__conn=None
            raise ConnectionError

    def __close(self) -> None:
        """
        Méthode permettant de fermer le curseur en même temps que la connexion à la base de données.
        """
        self.__cursor.close()
        self.__conn.close()

    def __closeCursor(self) -> None:
        """
        Méthode permettant de fermer le curseur.
        """
        self.__cursor.close()

    def __closeConn(self) -> None:
        """
        Méthode permettant de fermer la connexion à la base de données.
        """
        self.__conn.close()

    def __execute(self,
                query:str,
                data:list[str]=None):
        """
        Méthode permettant de souemttre une requête SQL à la base de données.

        :param query: La requête SQL "template"
        :type query: str
        :param data: les arguments à passer dans la requêtes SQL.
        :type data: list[str]
        """
        if data is None:
            data = {}
        self.__cursor.execute(query, data)
        self.__conn.commit()

    def executeSelect(self,
                      query:str,
                      data:list[str]=None):
        """
        Méhode permettant de soumettre une requpete de type SELECT à la base de données.
        Cette méthode retourne une liste de tuples. Correspondant au contenu du curseur.

        :param query: La requête SQL template de type SELECT
        :type query: str
        :param data: Les arguments à passer dans la requête SQL.
        :type data: list[str]

        :return: Une liste de tuples correspondant au contenu du curseur.
        """
        if data is None:
            data = {}
        self.__connect()
        self.__cursor.execute(query, data)
        self.__conn.commit()
        try:
            reponses = self.__cursor.fetchall()
        except:
            reponses = []
        self.__close()
        return reponses

    def executeInsert(self,
                      query: str,
                      data: list[str] = None) -> None:
        """
        Méthode pour executer une requête de type INSERT.

        :param query: la requête SQL template de type SELECT.
        :param data: Les arguments à passer dans la requête SQL.
        """
        if data is None:
            data = []
        self.__connect()
        self.__cursor.execute(query, data)
        self.__conn.commit()
        self.__close()

