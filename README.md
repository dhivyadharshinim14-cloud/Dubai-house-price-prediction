# Dubai House Price Prediction

## Project Overview

This machine learning project predicts property prices in Dubai using property characteristics such as bedrooms, bathrooms, area, property type, furnishing, completion status, and purpose.

The project includes data cleaning, exploratory data analysis, machine learning model training, evaluation, and a Streamlit web application.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

## Machine Learning Model

A Random Forest Regressor was used to predict Dubai property prices.

Categorical variables were processed using One-Hot Encoding, and numerical features were passed through a Scikit-learn preprocessing pipeline.

## Model Performance

- MAE: AED 1,448,968.90
- RMSE: AED 6,526,700.70
- R² Score: 0.706

The model achieved an R² score of approximately 70.6% on the test data.

## Key Features

- Bedrooms
- Bathrooms
- Area (sqft)
- Property Type
- Furnishing
- Completion Status
- Purpose

## Streamlit Application

The project includes a Streamlit application that allows users to enter property details and receive an estimated Dubai property price.

Example:

**2 bedrooms + 2 bathrooms + 1,200 sqft apartment → approximately AED 3.21 million**

## Project Structure

```text
Dubai-House-Price-Prediction/
│
├── data/
├── models/
├── notebooks/
├── src/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore