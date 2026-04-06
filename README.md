# 🎯 Customer Churn Prediction System (End-to-End Analytics)

## 📊 Python, Machine Learning & Power BI Analytics Project

---

## 🪄 Introduction

This project focuses on predicting customer churn using machine learning and advanced analytics techniques. It covers the full data lifecycle — from messy raw data to executive-level dashboards and business insights.

The analysis simulates a real-world business scenario in a **Retail Banking / Subscription-based environment**, demonstrating how data analytics drives retention strategies, revenue protection, and decision-making at the executive level.

---

## 📊 Badges

![GitHub repo size](https://img.shields.io/github/repo-size/cwalton133/customer-churn-prediction-system)
![License](https://img.shields.io/github/license/cwalton133/customer-churn-prediction-system)
![GitHub top language](https://img.shields.io/github/languages/top/cwalton133/customer-churn-prediction-system)

---

## 🧭 Business Context

Customer churn is one of the most critical challenges for subscription-based and financial service businesses.

Organizations face increasing pressure to:

- Reduce customer attrition
- Identify high-risk churn segments early
- Protect recurring revenue streams
- Improve customer lifetime value (CLV)
- Enable data-driven retention strategies

This project simulates how an organization can leverage data to **proactively predict churn and take action before revenue is lost**.

---

## 🎯 Purpose of the Project

The goal of this project is to build an **end-to-end churn prediction system** that:

- Identifies customers likely to churn
- Quantifies revenue at risk
- Segments customers based on value and behavior
- Provides actionable insights through dashboards

---

## 📈 Expected Outcomes

- A **machine learning model** predicting churn risk
- Identification of **key churn drivers**
- Revenue impact analysis (Revenue at Risk)
- A **Power BI dashboard** for executive decision-making
- A scalable analytics pipeline for real-world applications

---

## ⚠️ Disclaimer

This dataset is used strictly for **learning and portfolio purposes**.

- It does not represent real customer data
- All scenarios are simulated or anonymized

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset Description](#-dataset-description)
- [Methodology (CRISP-DM)](#-methodology-crisp-dm)
- [Data Pipeline](#-data-pipeline)
- [Machine Learning Model](#-machine-learning-model)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key KPIs & Metrics](#-key-kpis--metrics)
- [Key Insights](#-key-insights)
- [Strategic Recommendations](#-strategic-recommendations)
- [Tools & Technologies](#-tools--technologies)
- [Conclusion](#-conclusion)
- [Author](#-author)

---

## 🧭 Project Overview

This project demonstrates how raw customer data can be transformed into:

- Predictive intelligence
- Business insights
- Executive dashboards

The focus is on **business impact**, not just model performance.

---

## 🗂️ Dataset Description

The dataset includes customer-level information such as:

- **CustomerID** – Unique identifier
- **Demographics** – Gender, Dependents, Partner
- **Account Info** – Tenure, Contract Type, Payment Method
- **Services** – Internet, Phone, Streaming services
- **Financials** – Monthly Charges, Total Charges
- **Target Variable** – Churn (Yes/No)

---

📄 **Dataset Location:**  
👉 `data/raw/messy_churn.csv`

---

## 🔍 Methodology (CRISP-DM)

This project follows the **CRISP-DM framework**:

1. Business Understanding – Define churn problem
2. Data Understanding – Explore patterns & anomalies
3. Data Preparation – Clean and structure messy data
4. Feature Engineering – Create meaningful business features
5. Modeling – Train churn prediction model
6. Evaluation – Validate model performance
7. Deployment – Dashboard & reporting

---

## ⚙️ Data Pipeline

### 🔹 Step 1: Data Cleaning (`data_cleaning.py`)
- Removed duplicates
- Handled missing values
- Fixed inconsistent categories
- Created:
  - `has_internet`
  - `has_phone`
- Standardized service columns

---

### 🔹 Step 2: Feature Engineering (`feature_engineering.py`)
- Created:
  - Customer Lifetime Value (CLV)
  - Average Revenue
  - High Value Customers
  - Loyal Customers

---

### 🔹 Step 3: Model Training (`train_model.py`)
- Model: Random Forest Classifier
- Train/Test Split: 80/20
- Evaluation:
  - Accuracy
  - Classification Report
- Extracted Feature Importance

---

## 🤖 Machine Learning Model

The model predicts customer churn and identifies key drivers such as:

- Contract type
- Tenure
- Monthly charges
- Customer value segment

---

## 📊 Power BI Dashboard

> 📸 **Dashboard Preview Placeholder**  
> _Insert screenshot here_  
> **Suggested path:** `/dashboard/churn_dashboard.png`

The dashboard includes:

- KPI Cards:
  - Total Customers
  - Churn Rate
  - Revenue at Risk
- Churn Drivers:
  - Contract Type
  - Tenure Groups
- Customer Segmentation
- High-Risk Customer Table
- Interactive Filters

---

## 📌 Key KPIs & Metrics

- Churn Rate
- Revenue at Risk
- Customer Lifetime Value (CLV)
- Average Monthly Charges
- High-Value Customer Ratio

---

## 💡 Key Insights

- Month-to-month customers show the highest churn rate
- Customers with low tenure are more likely to churn
- High-value but non-loyal customers pose the highest revenue risk
- Service usage impacts retention significantly

---

## 🧠 Strategic Recommendations

1. Target **high-value, low-tenure customers** with retention offers  
2. Incentivize **long-term contracts**  
3. Improve onboarding experience for new customers  
4. Use segmentation for personalized retention strategies  
5. Monitor churn drivers continuously via dashboard  

---

## 🧰 Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn)
- SQL (conceptual workflow)
- Power BI (dashboard & storytelling)
- VS Code / Jupyter Notebook
- Git & GitHub

---

## 🏁 Conclusion

This project demonstrates how combining **data engineering, machine learning, and business intelligence** can create a powerful system for predicting churn and driving strategic decisions.

It reflects real-world analytics workflows used in consulting, banking, and SaaS environments.

---

## 📁 GitHub Repository Structure

```text
churn_prediction_project/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── train_model.py
│
├── dashboard/
│   └── churn_dashboard.pbix
│
├── model.pkl
├── requirements.txt
└── README.md