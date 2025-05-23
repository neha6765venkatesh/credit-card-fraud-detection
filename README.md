# 💳 Credit Card Fraud Detection App

A Machine Learning-based web application for detecting fraudulent credit card transactions using **anomaly detection** techniques and **XGBoost** classification.

---

## 📌 Project Overview

This project is designed to:
- Preprocess real-world credit card transaction data
- Detect anomalies using Isolation Forest and Local Outlier Factor
- Train a powerful classifier (XGBoost) to distinguish fraudulent vs non-fraudulent transactions
- Display predictions in a user-friendly Streamlit web interface

---

## 🚀 Features

- 📊 Exploratory data analysis and model training in Jupyter Notebook
- 🧠 Fraud detection using XGBoost classifier
- 📉 ROC curve plotting and model evaluation
- 🌐 Interactive Streamlit web app for predictions
- 🔒 Trained model saved and reused via `.pkl` file
- 🧰 Modular code structure (utils.py, app.py)

---

## 🗂️ Project Structure

creditfraud/
│
├── app/
│ ├── app.py # Streamlit app UI
│ └── utils.py # Prediction and preprocessing logic
│
├── data/
│ └── creditcard.csv # Dataset (not pushed to GitHub)
│
├── models/
│ └── xgboost_model.pkl # Trained ML model
│
├── notebook/
│ └── fraud_detection.ipynb # EDA, training, ROC curve
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧠 Models Used

- **Isolation Forest** (unsupervised anomaly detection)
- **Local Outlier Factor (LOF)** (unsupervised anomaly detection)
- **XGBoost Classifier** (supervised ML model)

---

## 📈 Model Evaluation

- ✅ ROC Curve
- ✅ Confusion Matrix
- ✅ Accuracy, Precision, Recall
- ✅ Feature importance plot (if applicable)

---

## 🛠️ How to Run the Project

### 🔹 Install dependencies

```bash
pip install -r requirements.txt
🔹 Run Jupyter Notebook
Navigate to the notebook folder:

bash
Copy
Edit
cd notebook
jupyter notebook
Open and run fraud_detection.ipynb to retrain the model and generate evaluation metrics.

🔹 Launch the Streamlit App
From the project root:

bash
Copy
Edit
streamlit run app/app.py
📬 Inputs to Streamlit App
The app takes transaction details such as:

Merchant category

Cardholder gender

Transaction amount

Latitude & longitude

City population

Job category

Then it predicts whether the transaction is fraudulent or not.

📦 Requirements
All dependencies are listed in requirements.txt. Major ones:

pandas

scikit-learn

xgboost

joblib

streamlit

matplotlib

🙌 Acknowledgements
Dataset: Kaggle - Credit Card Fraud Detection

Built with  using Python, Scikit-learn, and Streamlit

📸 Screenshot
![Fraud Detection Screenshot](![creditImage jpg](https://github.com/user-attachments/assets/87d6acb0-0b09-4f23-9bf0-1cdb935d4c2a))




