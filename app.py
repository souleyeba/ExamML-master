import gradio as gr
import pickle
import numpy as np

# Fonction pour charger le modèle
def load_model():
    model_path = "RandomForestClassifier_model.pkl"  # Chemin relatif au modèle
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Charger le modèle une fois lors du démarrage de l'application
model = load_model()

# Fonction de prédiction
def predict_survival(stay_class, sex, ticket_price):
    # Convertir 'Homme' et 'Femme' en 0 et 1 respectivement
    sex_numeric = 0 if sex == "Homme" else 1
    
    # Préparation des données pour le modèle
    data = np.array([[stay_class, sex_numeric, ticket_price]])
    
    # Faire une prédiction
    prediction = model.predict(data)
    survival = prediction[0]
    
    # Convertir la prédiction en texte lisible
    if survival == 1:
        return "Yes! la prédiction de survie du passager est positive (Oui)"
    else:
        return "Oups, la prédiction de survie du passager est négative (Non)"

# Créer l'interface Gradio
iface = gr.Interface(
    fn=predict_survival,
    inputs=[
        gr.Dropdown(choices=[1, 2, 3], label="Classe de séjour"),
        gr.Radio(choices=["Homme", "Femme"], label="Sexe"),
        gr.Number(label="Prix du ticket")
    ],
    outputs=gr.Textbox(),
    title="Prédiction de survie d'un passager du Titanic",
    description="Interface de prédiction de la survie d'un passager du Titanic avaec un modèle de machine learning"
)

# Lancer l'application Gradio
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)