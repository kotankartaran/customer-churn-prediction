# 📊 Customer Churn Prediction System

A Machine Learning-powered web application that predicts whether a telecom customer is likely to churn (leave the company) based on customer demographics, account information, and service usage patterns.

Built using **Python, Scikit-Learn, Streamlit, and Plotly**.

---

## 🚀 Project Overview

Customer churn is a major challenge for telecom companies. Retaining existing customers is often more cost-effective than acquiring new ones.

This project uses the **IBM Telco Customer Churn Dataset** and a **Random Forest Classifier** to predict customer churn and provide actionable insights through an interactive dashboard.

---

## 🎯 Objectives

* Predict customer churn using Machine Learning
* Identify key factors influencing churn
* Visualize customer risk through an interactive dashboard
* Help businesses improve customer retention strategies

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Plotly
* Joblib

---

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

**Total Records:** 7043 Customers

**Features Used:** 30

The dataset contains information such as:

* Gender
* Senior Citizen Status
* Partner Status
* Dependents
* Tenure
* Contract Type
* Monthly Charges
* Total Charges
* Internet Services
* Payment Method
* Churn Status

---

## 🤖 Machine Learning Model

### Algorithm

Random Forest Classifier

### Why Random Forest?

* Handles categorical and numerical data effectively
* Reduces overfitting
* Provides feature importance scores
* Delivers strong performance on classification tasks

---

## 📈 Model Performance

| Metric           | Value  |
| ---------------- | ------ |
| Accuracy         | 80.20% |
| Training Samples | 5634   |
| Testing Samples  | 1409   |
| Features         | 30     |

### Classification Report

| Class    | Precision | Recall | F1-Score |
| -------- | --------- | ------ | -------- |
| No Churn | 0.84      | 0.90   | 0.87     |
| Churn    | 0.66      | 0.52   | 0.58     |

---

## 🔥 Top Features Affecting Churn

1. Tenure
2. Total Charges
3. Monthly Charges
4. Internet Service (Fiber Optic)
5. Electronic Check Payment Method
6. Contract Type
7. Online Security
8. Technical Support
9. Paperless Billing
10. Partner Status

---

## 📊 Dashboard Features

✅ Customer Churn Prediction

✅ Churn Probability Score

✅ Stay Probability Score

✅ Risk Meter

✅ Interactive Pie Chart

✅ Feature Importance Visualization

✅ Customer Summary Table

---

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── train.py
├── requirements.txt
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   ├── churn_model.pkl
│   ├── feature_columns.pkl
│   └── feature_importance.csv
│
└── .gitignore
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Training

```bash
python train.py
```

---

## 🌐 Run Dashboard

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Sample Dashboard

Features included:

* Churn Prediction
* Risk Analysis
* Probability Visualization
* Feature Importance Chart
* Customer Analytics Dashboard

---

## 📚 Future Improvements

* Hyperparameter Tuning
* XGBoost / LightGBM Models
* Customer Segmentation
* Model Deployment on Cloud
* Real-time Predictions
* User Authentication

---

## 👨‍💻 Author

**Taran Kotankar**



---

## 📜 License

This project is created for educational and learning purposes.
