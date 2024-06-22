import streamlit as st
import pandas as pd
import pickle

# Title of the application
st.title("Heart Disease Prediction")

# Load the model
model = pickle.load(open("best_model_heart_disease_prediction.pkl", "rb"))

# Sidebar with user inputs
st.sidebar.header("User Input Features")

# Function to get user input
def get_user_input():
    age = st.sidebar.slider("Age", 18, 100, 25)
    sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
    cp = st.sidebar.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    trestbps = st.sidebar.slider("Resting Blood Pressure (mm Hg)", 90, 200, 120)
    chol = st.sidebar.slider("Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
    restecg = st.sidebar.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 150)
    exang = st.sidebar.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.sidebar.slider("ST Depression Induced by Exercise", 0.0, 6.2, 0.0)
    slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.sidebar.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
    thal = st.sidebar.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])


     # Encode categorical variables
    sex = 1 if sex == "Male" else 0
    cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
    fbs = 1 if fbs == "True" else 0
    restecg = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(restecg)
    exang = 1 if exang == "Yes" else 0
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)
    
    # Store the user input in a dictionary
    user_data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    return user_data

# Get user input
user_input = get_user_input()

# Display the user input
st.subheader("User Input:")
st.write(user_input)

# Make prediction
if st.sidebar.button('Predict'):
    input_data = [['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write('The patient is likely to have heart disease.')
    else:
        st.write('The patient is unlikely to have heart disease.')
