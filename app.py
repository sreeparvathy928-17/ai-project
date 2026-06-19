import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('delay_model.pkl', 'rb'))

st.title("🚍 Public Transit Delay Predictor")

rainfall = st.number_input(
    "Enter Rainfall (mm)",
    min_value=0.0,
    value=0.0
)

if st.button("Predict Delay"):
    prediction = model.predict(
        pd.DataFrame([[rainfall]], columns=['Rainfall_mm'])
    )

    st.success(
        f"Predicted Delay: {prediction[0]:.2f} minutes"
    )