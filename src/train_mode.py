import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# -------------------------------
# 1. Load featured data
# -------------------------------
df = pd.read_csv("data/processed/featured_churn.csv")

# -------------------------------
# 2. Prepare data
# -------------------------------

# Separate target
X = df.drop(columns=['churn', 'customerid'], errors='ignore')
y = df['churn']

# Encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# -------------------------------
# 3. Train/Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 4. Train Model
# -------------------------------
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------------
# 5. Evaluate Model
# -------------------------------
y_pred = model.predict(X_test)

print("✅ Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -------------------------------
# 6. Feature Importance (🔥 KEY)
# -------------------------------
importances = pd.Series(model.feature_importances_, index=X.columns)
top_features = importances.sort_values(ascending=False).head(10)

print("\n🔥 Top 10 Important Features:")
print(top_features)

# Save feature importance
top_features.to_csv("data/processed/feature_importance.csv")

# -------------------------------
# 7. Save Model
# -------------------------------
joblib.dump(model, "model.pkl")

print("\n✅ Model saved as model.pkl")