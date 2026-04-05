import pandas as pd
import numpy as np

def clean_data(messy_data):
    df = pd.read_csv(messy_data)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove duplicates
    df = df.drop_duplicates()

    # Fix categorical values
    df['internetservice'] = df['internetservice'].str.strip().str.capitalize()
    df['paymentmethod'] = df['paymentmethod'].str.strip().str.capitalize()
    df['gender'] = df['gender'].str.capitalize()

    # Convert TotalCharges to numeric
    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')

    # Handle missing values
    df['totalcharges'].fillna(df['monthlycharges'] * df['tenure'], inplace=True)
    df['tenure'].fillna(df['tenure'].median(), inplace=True)

    # Fix outliers (MonthlyCharges too high)
    df['monthlycharges'] = np.where(
        df['monthlycharges'] > df['monthlycharges'].quantile(0.99),
        df['monthlycharges'].median(),
        df['monthlycharges']
    )

    # Encode target
    df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})

    return df

if __name__ == "__main__":
    # Call the function with your specific file path
    df = clean_data("data/raw/messy_churn.csv")
    df.to_csv("data/processed/cleaned_churn.csv", index=False)