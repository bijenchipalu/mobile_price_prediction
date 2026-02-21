import streamlit as st
import pickle
import pandas as pd

# Load model and features
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.title("📱 Mobile Price Prediction System")
st.write("Select Mobile Specifications")

# Dropdown options for each feature
options = {

    "Sale": [1000, 3000, 5000, 8000, 10000],

    "weight": [150, 160, 170, 180, 190, 200, 210],

    "resoloution": [1280, 1920, 2160, 2400, 2560, 3200],

    "ppi": [250, 300, 350, 400, 450, 500],

    "cpu core": [2, 4, 6, 8],

    "cpu freq": [1.5, 1.8, 2.0, 2.2, 2.5, 3.0],

    "internal mem": [16, 32, 64, 128, 256, 512],

    "ram": [2, 4, 6, 8, 12, 16],

    "RearCam": [8, 12, 16, 32, 48, 64, 108],

    "Front_Cam": [5, 8, 12, 16, 32],

    "battery": [2500, 3000, 4000, 4500, 5000, 6000],

    "thickness": [6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
}

inputs = {}

# Create dropdowns
for col in features:

    label = col.replace("_", " ").title()

    inputs[col] = st.selectbox(
        f"{label}",
        options[col]
    )


# Predict Button
if st.button("🔍 Predict Price"):

    df = pd.DataFrame([inputs])

    price = model.predict(df)

    st.success(f"💰 Estimated Price: Rs. {int(price[0])}")