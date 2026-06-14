import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print("Original Shape:", df.shape)

# ==========================
# DATA CLEANING
# ==========================

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

df.drop(
    "customerID",
    axis=1,
    inplace=True
)

# ==========================
# TARGET ENCODING
# ==========================

df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# ==========================
# ONE HOT ENCODING
# ==========================

df = pd.get_dummies(
    df,
    drop_first=True
)

print("\nDataset After One-Hot Encoding:")
print(df.head())

# ==========================
# FEATURES & TARGET
# ==========================

X = df.drop(
    "Churn",
    axis=1
)

y = df["Churn"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ==========================
# TUNED RANDOM FOREST
# ==========================

model = RandomForestClassifier(
    n_estimators=500,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features="sqrt",
    bootstrap=True,
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)

# ==========================
# EVALUATION
# ==========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

# ==========================
# SAVE MODEL
# ==========================

joblib.dump(
    model,
    "models/churn_model.pkl"
)

# Save column names too
joblib.dump(
    X.columns.tolist(),
    "models/feature_columns.pkl"
)

print("\nModel saved successfully!")
print("Feature columns saved successfully!")

# ==========================
# FEATURE IMPORTANCE
# ==========================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 15 Important Features:")
print(
    importance.head(15).to_string(index=False)
)

importance.to_csv(
    "models/feature_importance.csv",
    index=False
)

print("\nFeature importance saved!")