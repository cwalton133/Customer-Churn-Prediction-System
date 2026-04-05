import pandas as pd

def create_features(df):

    # -------------------------------
    # Feature Engineering
    # -------------------------------

    # Customer lifetime value proxy
    df['clv'] = df['monthlycharges'] * df['tenure']

    # Average revenue
    df['avg_revenue'] = df['totalcharges'] / (df['tenure'] + 1)

    # High value customer
    df['high_value'] = (df['monthlycharges'] > df['monthlycharges'].median()).astype(int)

    # Long-term customer
    df['loyal_customer'] = (df['tenure'] > 24).astype(int)

    return df


if __name__ == "__main__":

    # 🔥 LOAD cleaned data
    df = pd.read_csv("data/processed/cleaned_churn.csv")

    # 🔥 APPLY feature engineering
    df = create_features(df)

    # 🔥 SAVE new dataset
    df.to_csv("data/processed/featured_churn.csv", index=False)

    print("✅ Feature engineering completed!")