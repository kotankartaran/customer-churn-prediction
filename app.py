import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("models/churn_model.pkl")

importance = pd.read_csv(
    "models/feature_importance.csv"
)

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("📋 Project Information")

st.sidebar.success("""
Customer Churn Prediction System

🎯 Objective:
Predict customer churn using machine learning.

🤖 Algorithm:
Random Forest Classifier

📊 Dataset:
IBM Telco Customer Churn Dataset

📈 Accuracy:
80.20%

🛠 Technologies:
• Python
• Pandas
• Scikit-Learn
• Streamlit
• Plotly
""")

# ==========================
# TITLE
# ==========================

st.title("📈 Telecom Customer Churn Analytics Dashboard")

st.markdown("""
Predict whether a telecom customer is likely to leave the company using Machine Learning.
""")

st.divider()

# ==========================
# INPUT SECTION
# ==========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

with col2:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

# ==========================
# PREDICT BUTTON
# ==========================

if st.button(
    "🔍 Predict Churn",
    width="stretch"
):

    # ==========================
    # CREATE FEATURE VECTOR
    # ==========================

    features = {
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,

        "gender_Male":
        1 if gender == "Male" else 0,

        "Partner_Yes":
        1 if partner == "Yes" else 0,

        "Dependents_Yes":
        1 if dependents == "Yes" else 0,

        "PhoneService_Yes": 1,

        "MultipleLines_No phone service": 0,
        "MultipleLines_Yes": 0,

        "InternetService_Fiber optic": 0,
        "InternetService_No": 0,

        "OnlineSecurity_No internet service": 0,
        "OnlineSecurity_Yes": 0,

        "OnlineBackup_No internet service": 0,
        "OnlineBackup_Yes": 0,

        "DeviceProtection_No internet service": 0,
        "DeviceProtection_Yes": 0,

        "TechSupport_No internet service": 0,
        "TechSupport_Yes": 0,

        "StreamingTV_No internet service": 0,
        "StreamingTV_Yes": 0,

        "StreamingMovies_No internet service": 0,
        "StreamingMovies_Yes": 0,

        "Contract_One year":
        1 if contract == "One year" else 0,

        "Contract_Two year":
        1 if contract == "Two year" else 0,

        "PaperlessBilling_Yes":
        1 if paperless == "Yes" else 0,

        "PaymentMethod_Credit card (automatic)": 0,
        "PaymentMethod_Electronic check": 1,
        "PaymentMethod_Mailed check": 0
    }

    features = pd.DataFrame([features])

    # ==========================
    # PREDICTION
    # ==========================

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    stay_probability = 1 - probability

    st.divider()

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )

    with metric2:
        st.metric(
            "Stay Probability",
            f"{stay_probability * 100:.2f}%"
        )

    # ==========================
    # RISK METER
    # ==========================

    st.subheader("Risk Meter")

    st.progress(
        float(probability)
    )

    if probability < 0.30:
        st.success("🟢 Low Risk Customer")

    elif probability < 0.60:
        st.warning("🟡 Medium Risk Customer")

    else:
        st.error("🔴 High Risk Customer")

    # ==========================
    # FINAL RESULT
    # ==========================

    if prediction == 1:

        st.error(
            f"⚠️ Customer is likely to churn "
            f"({probability * 100:.2f}% risk)"
        )

    else:

        st.success(
            f"✅ Customer is likely to stay "
            f"({stay_probability * 100:.2f}% confidence)"
        )

    # ==========================
    # PIE CHART
    # ==========================

    st.subheader(
        "Prediction Distribution"
    )

    pie_df = pd.DataFrame({
        "Category": [
            "Stay",
            "Churn"
        ],
        "Percentage": [
            stay_probability * 100,
            probability * 100
        ]
    })

    fig = px.pie(
        pie_df,
        names="Category",
        values="Percentage",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # ==========================
    # FEATURE IMPORTANCE
    # ==========================

    st.subheader(
        "Top Features Affecting Churn"
    )

    top_features = importance.head(10)

    fig2 = px.bar(
        top_features,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top 10 Important Features"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

    # ==========================
    # CUSTOMER SUMMARY
    # ==========================

st.subheader("Customer Summary")

summary_df = pd.DataFrame({
    "Feature": [
        "Gender",
        "Senior Citizen",
        "Partner",
        "Dependents",
        "Tenure (Months)",
        "Monthly Charges",
        "Total Charges",
        "Contract Type"
    ],
    "Value": [
        gender,
        senior,
        partner,
        dependents,
        f"{tenure}",
        f"${monthly_charges:.2f}",
        f"${total_charges:.2f}",
        contract
    ]
})

summary_df["Value"] = summary_df["Value"].astype(str)

st.dataframe(
    summary_df,
    width="stretch",
    hide_index=True
)