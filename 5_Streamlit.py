import pandas as pd
import streamlit as st
import pickle

# Charger le modèle entraîné
with open('data/trained_pipe.pkl', 'rb') as f:
    model = pickle.load(f)

df = pd.read_csv('data/cars_infos_cleaned.csv')

# Créer un formulaire Streamlit pour saisir les données d'entrée
st.write('## Prédiction de prix de voitures')
marque = st.selectbox('Marque', df.Marque.unique())
modele = st.text_input('Modèle')
classe = st.selectbox('Classe', df.Classe.unique())
portes = st.selectbox('Nombre de portes', [3,5])
longueur = st.number_input('Longueur (cm)', min_value=0.0, max_value=700.0, step=1.0)
hauteur = st.number_input('Hauteur (cm)', min_value=0.0, max_value=300.0, step=1.0)
largeur = st.number_input('Largeur (cm)', min_value=0.0, max_value=300.0, step=1.0)
empattement = st.number_input('Empattement (cm)', min_value=0.0, max_value=600.0, step=1.0)
moteur = st.number_input('Moteur (cm³)', min_value=0.0, max_value=8000.0, step=1.0)
poids = st.number_input('Poids (t)', min_value=0.0, max_value=1.5, step=0.1)
carburant = st.selectbox('Type de carburant', df.Carburant.unique())
conso_ville = st.number_input('Consommation en ville (L/100km)', min_value=0.0, max_value=7.5, step=0.1)
conso_autoroute = st.number_input('Consommation sur autoroute (L/100km)', min_value=0.0, max_value=5.0, step=0.1)
position_moteur = st.selectbox('Position du moteur', df.PositionMoteur.unique())
transmission = st.selectbox('Transmission', df.Transmission.unique())
chevaux = st.number_input('Chevaux', min_value=0.0, max_value=150.0, step=1.0)
regime = st.number_input('Régime de pointe (tr/min)', min_value=0.0, max_value=5000.0, step=1.0)
#On prend la réponse sous forme de Oui, Non plutôt que True or False
turbo__ = st.selectbox('Turbo', ['Non', 'Oui'])
#On définit le dictionnaire
turbo_ = {'Oui':True,'Non':False}
#On transforme la réponse du selecteur
turbo = turbo_[turbo__]
cylindres = st.selectbox('Nombre de cylindres', df.Cylindres.unique())
injecteur = st.selectbox('Injecteur', df.Injecteur.unique())
type_moteur = st.selectbox('Type de moteur', df.TypeMoteur.unique())
alesage = st.number_input('Alésage (mm)', min_value=0.0, max_value=120.0, step=1.0)
piston = st.number_input('Piston (cm)', min_value=0.0, max_value=10.0, step=1.0)
taux_compression = st.number_input('Taux de compression', min_value=0.0, max_value=10.0, step=0.1)

# Prédire le prix avec les données saisies et afficher le résultat
# if st.button('Prédire le prix'):
    
def predire_prix():
    features = pd.DataFrame({
        'Marque': [marque], 
        'Modèle': [modele],
        'Classe': [classe],
        'Portes': [portes], 
        'Longueur(cm)': [longueur], 
        'Hauteur(cm)': [hauteur], 
        'Largeur(cm)': [largeur],
        'Empattement(cm)' : [empattement], 
        'Moteur(cm³)' : [moteur],
        'Poids(t)' : [poids], 
        'Carburant' : [carburant], 
        'ConsommationVille(L/100km)' : [conso_ville],
        'ConsommationAutoroute(L/100km)' : [conso_autoroute],
        'PositionMoteur' : [position_moteur],
        'Transmission' : [transmission],
        'Chevaux' : [chevaux],
        'Régime(tr/min)' : [regime], 
        'Turbo' : [turbo], 
        'Cylindres' : [cylindres], 
        'Injecteur' : [injecteur],
        'TypeMoteur' : [type_moteur], 
        'Alésage(mm)' : [alesage], 
        'Piston(cm)' : [piston], 
        'TauxCompression' : [taux_compression]
    })
    prediction = round(model.predict(features)[0])
    return prediction

if st.button('Prédire le prix'):
    prediction = predire_prix()
    st.write(f'Le prix prédit est de {prediction} $')