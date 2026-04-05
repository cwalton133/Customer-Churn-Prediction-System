import pandas as pd
import numpy as np

messy_data = "data/raw/messy_churn.csv"

def clean_data(messy_data):
    df = pd.read_csv(messy_data)

    # -------------------------------
    # 1. Standardize column names
    # -------------------------------
    df.columns = df.columns.str.strip().str.lower()

    # -------------------------------
    # 2. Remove duplicates
    # -------------------------------
    df = df.drop_duplicates()

    # -------------------------------
    # 3. Fix categorical values
    # -------------------------------
    df['internetservice'] = df['internetservice'].str.strip().str.capitalize()
    df['paymentmethod'] = df['paymentmethod'].str.strip().str.capitalize()
    df['gender'] = df['gender'].str.capitalize()

    # -------------------------------
    # 4. Convert TotalCharges to numeric
    # -------------------------------
    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')

    # -------------------------------
    # 5. Handle missing values
    # -------------------------------
    df['totalcharges'] = df['totalcharges'].fillna(df['monthlycharges'] * df['tenure'])
    df['tenure'] = df['tenure'].fillna(df['tenure'].median())

    # -------------------------------
    # 6. Fix outliers
    # -------------------------------
    df['monthlycharges'] = np.where(
        df['monthlycharges'] > df['monthlycharges'].quantile(0.99),
        df['monthlycharges'].median(),
        df['monthlycharges']
    )

    # -------------------------------
    # 7. HANDLE "No internet service" (🔥 IMPORTANT)
    # -------------------------------

    service_cols = [
        'onlinesecurity', 'onlinebackup', 'deviceprotection',
        'techsupport', 'streamingtv', 'streamingmovies'
    ]

    # Create business feature: has internet
    df['has_internet'] = (df['internetservice'] != 'No').astype(int)

    # Normalize service columns
    for col in service_cols:
        df[col] = df[col].replace('No internet service', 'No')
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    # -------------------------------
    # 8. Encode other binary columns (optional but recommended)
    # -------------------------------
    binary_cols = ['partner', 'dependents', 'phoneservice', 'paperlessbilling']

    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    # -------------------------------
    # 9. Encode target variable
    # -------------------------------
    df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})

    return df


if __name__ == "__main__":
    df = clean_data("data/raw/messy_churn.csv")
    df.to_csv("data/processed/cleaned_churn.csv", index=False)

    print("✅ Data cleaning completed successfully!")