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

Vous pouvez installer ces modules en exécutant la commande suivante :

pip install -r requirements.txt

Description des fichiers

Le projet est organisé comme suit :

    data: ce dossier contient les données brutes du projet sous le nom "car_infos.csv", ainsi que le rapport de profilage généré par le notebook "1_Report.ipynb" sous le nom "csv_profile_report.html" et le fichier nettoyé "car_infos_cleaned.csv" obtenu grâce au notebook "2_Nettoyage.ipynb".

    notebooks: ce dossier contient les notebooks utilisés pour la préparation, l'analyse et la modélisation des données.

    pickle: ce dossier contient le modèle entraîné via la régression linéaire et enregistré grâce au notebook "4_Modelisation.ipynb".

    5_Streamlit.py: ce fichier contient le code permettant de lancer l'application Streamlit. Ce fichier utilise le modèle enregistré dans le dossier "pickle" pour prédire le prix d'une voiture en fonction de ses caractéristiques.

Comment lancer l'application

Pour lancer l'application Streamlit, exécutez la commande suivante dans le terminal :

arduino

streamlit run 5_Streamlit.py

Cela va lancer l'application dans votre navigateur par défaut. Vous pouvez ensuite renseigner les caractéristiques de votre voiture pour obtenir une estimation de son prix.

Nous espérons que vous apprécierez cette application !