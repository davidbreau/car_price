## Estimation de prix d'une voiture

Dans le cadre de la formation en data et intelligence artificielle, il est demandé de créer une application permettant de prédire le prix d'une voiture à partir de ses caractéristiques.

Avant de commencer, assurez-vous d'avoir installé les modules suivants :

    ipykernel
    pandas
    matplotlib
    seaborn
    scikit-learn
    streamlit
    pickle

Vous pouvez installer ces modules en exécutant la commande suivante sur le terminal :

~ pip install -r requirements.txt -Upgrade

Description des fichiers

Le projet est organisé comme suit :

data : ce dossier regroupe toutes les données. Le jeu de données brut qui a servi à commencer ce projet (cars_infos), son rapport de profilage (csv_profile_report) que vous pouvez ouvrir avec votre navigateur, la version nettoyée des données (cars_infos_cleaned), et enfin le pickle contenant le modèle d'entrainement(trained_pipe)

On y trouve ensuite :

Des notesbooks contenant la preparation, l'ananlyse et la modélisation des données :

1_Report : Ce fichier génèrel e rapport de profilage sur les données bruts du projet.
2_Nettoyage : Présentation du code permettant de traduire et nettoyer ces dites-données et les enregistres dans le dossier data.
3_Analyse : Reprend les données nettoyées et les explore grâce à des graphiques dans le but de voir les corrélation entre le prix et les caractèristiques de chaque voiture du jeu de données.
4_Modelisation : Depuis les données néttoyées, on crée un modèle d'entrainement grâce à une régression linaire, qu'on exporte ensuite dans le dossier data.

Un fichier python pour pouvoir lancer l'application
5_Streamlit : Ce fichier génère un formulaire pour obtenir estimation de prix.

Pour lancer l'application Streamlit, exécutez la commande suivante dans le terminal :

streamlit run 5_Streamlit.py

Cela va lancer l'application dans votre navigateur par défaut. Vous pouvez ensuite renseigner les caractéristiques de votre voiture pour obtenir une estimation de son prix.

Nous espérons que vous apprécierez cette application !
