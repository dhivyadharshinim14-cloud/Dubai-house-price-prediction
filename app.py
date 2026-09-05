import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("models/dubai_house_price_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Dubai House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# Title
st.title("🏠 Dubai House Price Prediction")

st.write(
    "Enter the property details below to estimate the "
    "property price in Dubai."
)


# User inputs
bedroom = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)

bathroom = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=13,
    value=2
)

area = st.number_input(
    "Area (sqft)",
    min_value=100,
    max_value=50000,
    value=1200
)

property_type = st.selectbox(
    "Property Type",
    [
        "Apartment",
        "Villa",
        "Townhouse",
        "Penthouse",
        "Villa Compound",
        "Residential Building"
    ]
)

furnishing = st.selectbox(
    "Furnishing",
    [
        "Furnished",
        "Unfurnished"
    ]
)

completion_status = st.selectbox(
    "Completion Status",
    [
        "Ready",
        "Off-Plan"
    ]
)

purpose = st.selectbox(
    "Purpose",
    [
        "Sale"
    ]
)


# Prediction
if st.button("Predict Price"):

    new_property = pd.DataFrame({
        "bedroom": [bedroom],
        "bathroom": [bathroom],
        "area(sqft)": [area],
        "propert_type": [property_type],
        "furnishing": [furnishing],
        "completion_status": [completion_status],
        "purpose": [purpose]
    })

    predicted_price = model.predict(new_property)

    st.success(
        f"Estimated Property Price: AED {predicted_price[0]:,.2f}"
    )