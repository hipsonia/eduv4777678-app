import streamlit as st
import joblib as joblib

# Load the trained model
model = joblib.load('best_model_heart_disease_prediction.pkl')

# Train and evaluate models
best_model = None
best_accuracy = 0

for name, model in models.items():
    model.fit(X_train_preprocessed, y_train)
    y_pred = model.predict(X_test_preprocessed)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} accuracy: {accuracy}")
    
    # Update best model
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

joblib.dump(best_model, 'best_model_heart_disease_prediction.pkl')




# Define the layout and widgets
st.title('Heart Disease Prediction')
st.sidebar.header('Patient Details')

age = st.sidebar.number_input('Age', min_value=1, max_value=120, value=25)
sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
cp = st.sidebar.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
trestbps = st.sidebar.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
chol = st.sidebar.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200)
fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
thalach = st.sidebar.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
exang = st.sidebar.selectbox('Exercise Induced Angina', ['No', 'Yes'])
oldpeak = st.sidebar.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=0.0)
slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
ca = st.sidebar.number_input('Number of Major Vessels Colored by Flourosopy', min_value=0, max_value=4, value=0)
thal = st.sidebar.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

# Convert categorical inputs to numerical
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'Yes' else 0
exang = 1 if exang == 'Yes' else 0
slope = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}[slope]
thal = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}[thal]

# Make prediction
if st.sidebar.button('Predict'):
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write('The patient is likely to have heart disease.')
    else:
        st.write('The patient is unlikely to have heart disease.')
