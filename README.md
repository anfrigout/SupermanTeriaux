# SupermanTeriaux
PAPPL - Projet plaque stratifiée

Ce document a pour obtectif de présenter la manière d'installer l'application sur son post de travail. 

## Installation de conda

Suivez la procédure d'installation de conda disponible ici : 
- Windows : https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html
- Mac : https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html

Pour vérifier que votre installation de conda est opérationnelle, ouvrez un terminal et lancé la commande suivante : 

```bash
conda --version
```

La version de votre installation doit s'afficher. 

## Installation de l'environnement

Vous devrez ensuite lancer l'installation de l'environnement conda, pour cela utilisez la commande suivante. 
Commencez par vous rendre dans le repertoire où vous avez téléchargé l'application.

```bash
conda env create -n SUPERMANTERIAUX --file bin/environment.yml
```

Une fois que l'environnement est créé, vous pouvez lancer la commande suivante pour activer l'environnement.

```bash
conda activate SUPERMANTERIAUX
```

## Modification du fichier de config de la base de données

Vous pouvez modifier le fichier conf/.database.proprieties afin de faire pointer vers votre base de données. Par défaut le fichier présent sur ce repo ne contient pas d'identifiants.

Vous devrez ensuite créer la table ***materiau*** à l'aide du fichier `sql/INIT_BDD.sql`

## Lancement de l'application

Pour ouvrir l'application, vous pouvez ensuite lancer la commande suivante :

```bash
python3 script/App.py
```
## Autres

Cette application est proposée gratuitement. Veuillez vous mettre en accord avec les licences des différents modules utilisés pour un usage commerciale. 
