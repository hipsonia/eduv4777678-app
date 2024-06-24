import streamlit as st
import pandas as pd
import numpy as np


# Title of the application
st.title("Heart Disease Prediction")


x = df 
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train,y_train)
  
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
    sex_encoded = 1 if sex == "Male" else 0
    cp_encoded = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
    fbs_encoded = 1 if fbs == "True" else 0
    restecg_encoded = ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"].index(restecg)
    exang_encoded = 1 if exang == "Yes" else 0
    slope_encoded = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal_encoded = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

    # Store the user input in a dictionary
    user_data = {
        "age": age,
        "sex": sex_encoded,
        "cp": cp_encoded,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs_encoded,
        "restecg": restecg_encoded,
        "thalach": thalach,
        "exang": exang_encoded,
        "oldpeak": oldpeak,
        "slope": slope_encoded,
        "ca": ca,
        "thal": thal_encoded
    }

    features = pd.DataFrame(user_data, index=[0])
    return features

# Get user input
input_df = get_user_input()

# Display the user input
st.subheader("User Input:")
st.write(input_df)

# Make prediction
if st.sidebar.button('Predict'):
    try:
        prediction = model.predict(input_df)
        if prediction[0] == 1:
            st.write('The patient is likely to have heart disease.')
        else:
            st.write('The patient is unlikely to have heart disease.')
    except Exception as e:
        st.error(f"Error making prediction: {e}")
