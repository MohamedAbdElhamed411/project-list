'''import streamlit as st
import joblib
import numpy as np

# Load model with error handling
try:
    model = joblib.load("baggingModel.pkl")
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Function to preprocess user input
def preprocess_input(WBC, LYMp, NEUTp, LYMn, NEUTn, RBC, HGB, HCT, MCV, MCH, MCHC, PLT, PDW, PCT):
    input_data = np.array([[WBC, LYMp, NEUTp, LYMn, NEUTn, RBC, HGB, HCT, MCV, MCH, MCHC, PLT, PDW, PCT]])
    return input_data

# Streamlit UI
st.title("🩸 Blood Test Diagnosis Prediction")
st.write("Enter your blood test parameters below to check for possible conditions.")

# User Inputs
WBC = st.number_input("WBC (White Blood Cells)", min_value=1.0, max_value=200.0, value=6.0, step=0.1)
LYMp = st.number_input("LYMp (Lymphocyte %)", min_value=0.0, max_value=100.0, value=30.0, step=0.1)
NEUTp = st.number_input("NEUTp (Neutrophil %)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
LYMn = st.number_input("LYMn (Lymphocyte #)", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
NEUTn = st.number_input("NEUTn (Neutrophil #)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
RBC = st.number_input("RBC (Red Blood Cells)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
HGB = st.number_input("HGB (Hemoglobin)", min_value=0.0, max_value=20.0, value=14.0, step=0.1)
HCT = st.number_input("HCT (Hematocrit)", min_value=0.0, max_value=60.0, value=42.0, step=0.1)
MCV = st.number_input("MCV (Mean Corpuscular Volume)", min_value=0.0, max_value=120.0, value=90.0, step=0.1)
MCH = st.number_input("MCH (Mean Corpuscular Hemoglobin)", min_value=0.0, max_value=40.0, value=30.0, step=0.1)
MCHC = st.number_input("MCHC (Mean Corpuscular Hemoglobin Concentration)", min_value=0.0, max_value=50.0, value=34.0, step=0.1)
PLT = st.number_input("PLT (Platelets)", min_value=0.0, max_value=1000.0, value=250.0, step=1.0)
PDW = st.number_input("PDW (Platelet Distribution Width)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
PCT = st.number_input("PCT (Plateletcrit)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

# Prediction button
if st.button("Predict Diagnosis"):
    with st.spinner("Analyzing... Please wait"):
        input_data = preprocess_input(WBC, LYMp, NEUTp, LYMn, NEUTn, RBC, HGB, HCT, MCV, MCH, MCHC, PLT, PDW, PCT)

        try:
            prediction = model.predict(input_data)[0]
            st.subheader(f"Predicted Diagnosis: 🏥 {prediction}")
        except Exception as e:
            st.error(f"❌ Prediction error: {e}")'''


import streamlit as st
import joblib
import numpy as np

# Apply custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        background-color: #F5F7FA;
    }
    .stApp {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .title {
        color: #007BFF;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        color: #444;
        text-align: center;
        font-size: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #007BFF;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("baggingModel.pkl")
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()

model = load_model()

# Streamlit UI
st.markdown("<h1 class='title'>🩸 Blood Test Diagnosis</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enter your blood test parameters below to check for possible conditions.</p>", unsafe_allow_html=True)
st.divider()

# Sidebar for additional information
st.sidebar.header("ℹ️ About the App")
st.sidebar.write("This AI-based system predicts blood-related conditions like anemia, thrombocytopenia, and leukemia.")
st.sidebar.write("🔍 Enter your blood test values, and get an instant AI-based diagnosis.")

st.sidebar.subheader("⚙️ How It Works")
st.sidebar.write("""
1️⃣ Input your blood test values.  
2️⃣ Click the 'Predict Diagnosis' button.  
3️⃣ Get your AI-generated diagnosis.  
""")

# User Inputs - Two Column Layout
st.subheader("🔍 Blood Test Parameters")
col1, col2 = st.columns(2)

with col1:
    WBC = st.number_input("WBC (White Blood Cells)", min_value=1.0, max_value=200.0, value=6.0, step=0.1)
    LYMp = st.number_input("LYMp (Lymphocyte %)", min_value=0.0, max_value=100.0, value=30.0, step=0.1)
    NEUTp = st.number_input("NEUTp (Neutrophil %)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
    LYMn = st.number_input("LYMn (Lymphocyte #)", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
    NEUTn = st.number_input("NEUTn (Neutrophil #)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
    RBC = st.number_input("RBC (Red Blood Cells)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    HGB = st.number_input("HGB (Hemoglobin)", min_value=0.0, max_value=20.0, value=14.0, step=0.1)

with col2:
    HCT = st.number_input("HCT (Hematocrit)", min_value=0.0, max_value=60.0, value=42.0, step=0.1)
    MCV = st.number_input("MCV (Mean Corpuscular Volume)", min_value=0.0, max_value=120.0, value=90.0, step=0.1)
    MCH = st.number_input("MCH (Mean Corpuscular Hemoglobin)", min_value=0.0, max_value=40.0, value=30.0, step=0.1)
    MCHC = st.number_input("MCHC (Mean Corpuscular Hemoglobin Concentration)", min_value=0.0, max_value=50.0, value=34.0, step=0.1)
    PLT = st.number_input("PLT (Platelets)", min_value=0.0, max_value=1000.0, value=250.0, step=1.0)
    PDW = st.number_input("PDW (Platelet Distribution Width)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
    PCT = st.number_input("PCT (Plateletcrit)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

# Prediction button with hover effect
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #007BFF;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("🔮 Predict Diagnosis"):
    with st.spinner("🔎 Analyzing... Please wait"):
        input_data = np.array([[WBC, LYMp, NEUTp, LYMn, NEUTn, RBC, HGB, HCT, MCV, MCH, MCHC, PLT, PDW, PCT]])
        
        try:
            prediction = model.predict(input_data)[0]
            st.subheader(f"Predicted Diagnosis is : 🔬 {prediction} 🏥")
        except Exception as e:
            st.error(f"❌ Prediction error: {e}")

# Footer
st.markdown("---")
st.markdown("🏥 Developed for AI-based healthcare solutions | © 2025")
