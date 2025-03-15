import streamlit as st
import joblib
import numpy as np

# Load model with error handling
try:
    model = joblib.load("RF.pkl")
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Function to preprocess user input
def preprocess_input(gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level):
    gender = float(1 if gender == "Male" else 0)
    
    # Convert input to NumPy array (must match the model's expected feature order)
    input_data = np.array([[gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level]])
    return input_data

# Streamlit UI
st.title("🩺 Diabetes Prediction App")
st.write("Enter your details below to check your risk of diabetes.")

# User Inputs
gender = st.radio("Gender", ("Male", "Female"))
age = st.number_input("Age", min_value=0, max_value=120, value=30)
hypertension = st.radio("Hypertension", (0, 1))
heart_disease = st.radio("Heart Disease", (0, 1))
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
HbA1c_level = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, value=5.5, step=0.1)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, value=100)

# Prediction button
if st.button("Predict Diabetes"):
    with st.spinner("Analyzing... Please wait"):
        input_data = preprocess_input(gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level)

        # Debugging: Ensure input shape matches model expectations
        st.write(f"✅ Input data shape: {input_data.shape}")  # Should be (1, 7)

        try:
            probability = model.predict_proba(input_data)[:, 1][0]  # Get probability for diabetic class

            threshold = 0.6  # Change this value to find the best threshold
            prediction = 1 if probability > threshold else 0

            result = "🩸 **Diabetic**" if prediction == 1 else "✅ **Non-Diabetic**"
            confidence = f"Confidence: **{probability * 100:.2f}%**"

            st.subheader(f"Prediction: {result}")
            st.write(confidence)

        except Exception as e:
            st.error(f"❌ Prediction error: {e}")
