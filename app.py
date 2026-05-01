import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Diabetes Prediction", layout="centered", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
        .stMetric {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🩺 Diabetes Prediction System")
st.write("This application uses a Machine Learning Ensemble model trained on the Pima Indians Diabetes Dataset to predict the likelihood of diabetes.")

# Load model and scaler
@st.cache_resource
def load_model():
    model = joblib.load('diabetes_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

try:
    model, scaler = load_model()
except FileNotFoundError:
    st.error("❌ Model files not found! Please ensure 'diabetes_model.pkl' and 'scaler.pkl' are in the same directory.")
    st.stop()

# Feature names (all features in order)
all_features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Top 6 features selected by SelectKBest (in the order they were selected)
top_features = ['Glucose', 'Insulin', 'BMI', 'SkinThickness', 'Age', 'Pregnancies']

# Sidebar for instructions
with st.sidebar:
    st.header("📋 Instructions")
    st.write("""
    1. Enter patient health metrics
    2. Click "Predict" button
    3. View results and confidence level
    
    **Note:** This is a predictive tool and should not be used as a substitute for professional medical diagnosis.
    """)
    
    st.header("ℹ️ About the Model")
    st.write("""
    - **Model Type:** Ensemble Voting Classifier
    - **Components:** SVM, Random Forest, XGBoost
    - **Accuracy:** 88.94% (10-fold CV) ± 3.48%
    - **Dataset:** Pima Indians Diabetes
    """)

# Main input form
st.header("Enter Patient Information")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=15, value=1, step=1)
    glucose = st.number_input('Glucose (mg/dL)', min_value=0, max_value=300, value=100, step=1)
    blood_pressure = st.number_input('Blood Pressure (mmHg)', min_value=0, max_value=200, value=70, step=1)
    skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=100, value=20, step=1)

with col2:
    insulin = st.number_input('Insulin (mu U/ml)', min_value=0, max_value=900, value=80, step=1)
    bmi = st.number_input('BMI (kg/m²)', min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5, step=0.01)
    age = st.number_input('Age (years)', min_value=18, max_value=100, value=35, step=1)

# Prediction Button
if st.button("🔮 Make Prediction", type="primary", use_container_width=True):
    # Prepare data with ALL features in correct order
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })
    
    # Select and order features as used in training
    input_selected = input_data[top_features]
    
    # Scale features
    input_scaled = scaler.transform(input_selected)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]
    
    # Display Results
    st.divider()
    st.header("📊 Prediction Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if prediction == 1:
            st.error("**POSITIVE** - Diabetes Detected")
        else:
            st.success("**NEGATIVE** - No Diabetes")
    
    with col2:
        confidence = probability[prediction] * 100
        st.metric("Confidence Level", f"{confidence:.2f}%")
    
    # Probability breakdown
    st.divider()
    st.subheader("Probability Breakdown")
    
    prob_col1, prob_col2 = st.columns(2)
    
    with prob_col1:
        st.write(f"**No Diabetes:** {probability[0]*100:.2f}%")
    with prob_col2:
        st.write(f"**Diabetes:** {probability[1]*100:.2f}%")
    
    # Risk level
    st.divider()
    risk_level = probability[1]
    
    if risk_level < 0.3:
        st.info("**Risk Level:** 🟢 Low - Continue regular health checks")
    elif risk_level < 0.6:
        st.warning("**Risk Level:** 🟡 Moderate - Consult healthcare provider")
    else:
        st.error("**Risk Level:** 🔴 High - Seek immediate medical attention")
    
    st.divider()
    st.caption("⚕️ Disclaimer: This prediction is for educational purposes only. Always consult a qualified healthcare professional for medical diagnosis and treatment.")

# Footer
st.divider()
st.markdown("""
---
*Built with Streamlit | Machine Learning Model: Ensemble Voting Classifier*
""")
