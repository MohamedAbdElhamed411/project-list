import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

# Load model
try:
    model = joblib.load("RF.pkl")
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Encoding mappings
sex_map = {"M": 1, "F": 0}
chest_pain_map = {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}
resting_ecg_map = {"Normal": 0, "ST": 1, "LVH": 2}
exercise_angina_map = {"N": 0, "Y": 1}
st_slope_map = {"Up": 0, "Flat": 1, "Down": 2}

# Custom style
st.markdown("""
    <style>
    .main {background-color: #f9f9f9;}
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        padding: 0.5em 1em;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("❤️ Heart Disease Prediction ")
st.markdown("This AI tool predicts the likelihood of heart disease based on clinical parameters. Provide the patient details below:")

# Input collection
with st.form("heart_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🧓 Age", min_value=1, max_value=120, value=40)
        sex = st.radio("⚧️ Sex", options=["M", "F"])
        cp = st.selectbox("💓 Chest Pain Type", options=["ATA", "NAP", "ASY", "TA"])
        bp = st.number_input("🩺 Resting BP", min_value=50, max_value=200, value=120)
        chol = st.number_input("🧪 Cholesterol (mg/dL)", min_value=0.0, max_value=600.0, value=200.0)

    with col2:
        fbs = st.radio("🍬 Fasting BS > 120 mg/dl?", options=[0, 1])
        ecg = st.selectbox("📉 Resting ECG", options=["Normal", "ST", "LVH"])
        maxhr = st.number_input("❤️ Max Heart Rate", min_value=60, max_value=250, value=150)
        exang = st.radio("🏃 Exercise-Induced Angina", options=["N", "Y"])
        oldpeak = st.number_input("📉 ST Depression (Oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
        slope = st.selectbox("📈 ST Slope", options=["Up", "Flat", "Down"])

    submitted = st.form_submit_button("🔍 Predict")

# Preprocessing
def preprocess_input(age, sex, cp, bp, chol, fbs, ecg, maxhr, exang, oldpeak, slope):
    return np.array([[age,
                      sex_map[sex],
                      chest_pain_map[cp],
                      bp,
                      chol,
                      fbs,
                      resting_ecg_map[ecg],
                      maxhr,
                      exercise_angina_map[exang],
                      oldpeak,
                      st_slope_map[slope]]])

# Prediction
if submitted:
    with st.spinner("Analyzing..."):
        try:
            input_data = preprocess_input(age, sex, cp, bp, chol, fbs, ecg, maxhr, exang, oldpeak, slope)
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]  # Assuming binary classification
            confidence = f"{probability * 100:.2f}%"
            st.markdown("---")
            if prediction == 1:
                st.subheader("❌ **High Risk of Heart Disease**")
                st.error(f"⚠️ **Recommendation:** Please consult a cardiologist.")
                st.markdown(f"📊 **Confidence:** `{confidence}`")
                st.markdown("💡 *Tip: Consider reducing stress, avoiding smoking, and managing blood pressure.*")
            else:
                st.subheader("✅ **Low Risk of Heart Disease**")
                st.success("🎉 You're in good shape! Keep living healthy.")
                st.markdown(f"📊 **Confidence:** `{confidence}`")
                st.markdown("💪 *Tip: Maintain a healthy diet and regular exercise.*")

        except Exception as e:
            st.error(f"❌ Prediction error: {e}")
