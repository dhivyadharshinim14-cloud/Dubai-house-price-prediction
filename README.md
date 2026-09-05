🏠 Dubai House Price Prediction

A machine learning project that predicts property prices in Dubai using property-related features and a Random Forest Regression model.

The project includes data preprocessing, exploratory data analysis, model training and evaluation, and a Streamlit web application for making property price predictions.

---

📌 Project Overview

Dubai's real estate market contains properties with widely varying prices depending on factors such as location, size, number of bedrooms, bathrooms, and property type.

The goal of this project is to build a machine learning model that can estimate the price of a Dubai property based on its characteristics.

Problem Statement

«Build a machine learning regression model capable of predicting Dubai property prices from historical property data.»

---

🎯 Objectives

- Clean and preprocess Dubai property data
- Perform exploratory data analysis (EDA)
- Identify important factors affecting property prices
- Train a machine learning regression model
- Evaluate model performance
- Save the trained model for reuse
- Build a Streamlit application for predictions
- Deploy the project in a user-friendly format

---

🛠️ Technologies Used

- Python
- Pandas – Data manipulation
- NumPy – Numerical computation
- Matplotlib – Data visualization
- Seaborn – Exploratory data analysis
- Scikit-learn – Machine learning
- Joblib – Model serialization
- Streamlit – Web application
- Jupyter Notebook – Development and experimentation
- Git & GitHub – Version control

---

📂 Project Structure

Dubai-house-price-prediction/
│
├── data/
│   └── dataset files
│
├── notebooks/
│   └── model development and analysis
│
├── models/
│   └── trained model
│
├── src/
│   └── source code
│
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

---

🔄 Machine Learning Workflow

Raw Property Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train / Test Split
        ↓
Random Forest Regression
        ↓
Model Evaluation
        ↓
Save Trained Model
        ↓
Streamlit Prediction App

---

🤖 Machine Learning Model

The project uses Random Forest Regression to predict property prices.

Random Forest was selected because it can model non-linear relationships between property characteristics and price and can capture interactions between multiple features.

---

📊 Model Evaluation

The model was evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

Test Set Results

Metric| Result
MAE| AED 1,448,968.90
RMSE| AED 6,526,700.70
R² Score| 0.706

The model achieved an R² score of 0.706 on the test set, indicating that the model explains approximately 70.6% of the variance in the target property prices.

«Note: R² is a model evaluation metric and should not be interpreted as prediction accuracy.»

---

🌐 Streamlit Application

The project includes a Streamlit application that allows users to enter property details and receive a predicted Dubai property price.

Example inputs include property characteristics such as:

- Location
- Property type
- Number of bedrooms
- Number of bathrooms
- Property size
- Other available property features

The application loads the trained machine learning model and generates a predicted property price.

---

🚀 How to Run the Project

1. Clone the repository

git clone https://github.com/dhivyadharshinim14-cloud/Dubai-house-price-prediction.git

2. Open the project folder

cd Dubai-house-price-prediction

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

---

💡 Key Learnings

Through this project, I gained practical experience in:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Regression modelling
- Random Forest
- Model evaluation
- Saving and loading machine learning models
- Building a Streamlit application
- Using Git and GitHub for version control

---

🔮 Future Improvements

Possible improvements include:

- Hyperparameter tuning
- Testing additional regression algorithms
- Feature selection and engineering
- Cross-validation
- Improving model performance
- Adding interactive visualizations
- Deploying the Streamlit application
- Adding more recent Dubai property data

---

👩‍💻 Author

Dhivyadharshini

Computer Science Engineering Graduate

---

📄 License

This project is licensed under the MIT License.