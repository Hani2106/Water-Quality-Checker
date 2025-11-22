import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Water Quality Checker", page_icon="💧")
st.title("💧 AI Water Quality Checker")

st.markdown("Enter water sample parameters below to check if it's **safe** or **unsafe** for drinking.")

# Input sliders
ph = st.slider("pH", 0.0, 14.0, 7.0)
hardness = st.slider("Hardness", 50.0, 400.0, 200.0)
solids = st.slider("Solids", 5000.0, 50000.0, 20000.0)
chloramines = st.slider("Chloramines", 0.0, 15.0, 7.0)
sulfate = st.slider("Sulfate", 100.0, 500.0, 300.0)
conductivity = st.slider("Conductivity", 100.0, 1000.0, 400.0)
organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 10.0)
trihalomethanes = st.slider("Trihalomethanes", 0.0, 120.0, 60.0)
turbidity = st.slider("Turbidity", 0.0, 10.0, 4.0)

if st.button("Check Water Quality"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])
    result = model.predict(input_data)
    if result[0] == 1:
        st.success("✅ The water is SAFE for drinking.")
    else:
        st.error("⚠️ The water is UNSAFE for drinking.")
