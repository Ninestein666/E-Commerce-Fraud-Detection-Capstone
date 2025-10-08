# E-Commerce Fraud Detection Capstone Project

This project involves the analysis of e-commerce transactional data to gather meaningful data and insights to help identify fraudulent transactions. The project encompasses data extraction, transformation, and loading (ETL), exploratory data analysis (EDA), and the creation of data visualizations to support findings.

The dataset contains various features related to transactions, including transaction amount, time, location, method of transaction, devices used, and whether a coupon was applied. The goal is to identify patterns and characteristics of fraudulent transactions to aid in fraud detection.

At a glance:
* Audience: Fraud operations / risk analysts (technical and non-technical)
* Goal: Identify when/where/how fraud occurs, communicate insights clearly, and propose practical controls to minimise fraud risks.
* Scope: Jupyter Notebooks for ETL, EDA, Data Visualisations and PowerBi Dashboard for interactive data exploration.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Dataset Source & Content
The dataset we are using was found on Kaggle:
https://www.kaggle.com/datasets/wafaaelhusseini/synthetic-fraud-transactions

The dataset contains the following:
- Transaction_ID: Unique identifier for each transaction
- User_ID: Unique identifier for each user (anonymised)
- Timestamp: Date and time of the transaction
- Amount: Monetary value of the transaction
- Country: Country where the transaction originated
- Device_Type: Type of device used for the transaction (e.g., mobile, desktop)
- Channel: Channel through which the transaction was made (e.g., web, app)
- Hour: Hour of the day when the transaction occurred
- Day_of_Week: Day of the week when the transaction occurred
- Coupon_Applied: Indicates whether a coupon was applied to the transaction (True/False)
- Is_Fraud: Indicates whether the transaction was fraudulent (1 for fraud, 0 for non-fraud) (True/False)
- Synthetic data generated to simulate real-world e-commerce transactions with no PII (Personally Identifiable Information).

# Stages of Main Files
- (Raw) Primary File: Dataset/Raw/transactions.csv
- (Cleaned) Transformed File: Dataset/Cleaned/cleaned_transactions.csv
- Enriched & Feature Engineered File: reports/tables/transaction_risk_scores.csv
- Power BI Dashboard File: PowerBI/E-Commerce Fraud Detection.pbix

# Project Purpose & Overview

This project delivers a lightweight analytics pipeline to support day-to-day fraud operations:
- ETL (Jupyter, Python): cleaned, standardised and validated raw data.
- EDA (Jupyter): discovered trends, patterns and anomalies. Also performed feature engineering. Mean, Median, Cohen's d test and grouping analysis.
- Notebook Visualisations: simple and easy to follow, reproducible plots (matplotlib/seaborn).
- Power BI Dashboard: interactive, business-ready views for decision-makers.

Key decisions enabled

- Thresholding: step-up checks for high-amount bands / high-risk bands.
- Scheduling: staff/rules during hot hours and peak day×hour pockets.
- Targeted controls: stricter checks for risky device×channel combos and countries.
- Promo safeguards: tighten coupon flows if fraud share is elevated.
- Peaks in fraud rates by time of day and day of week.

# Business Requirements

- Quantify fraud rates by time, location, device, channel, amount bands and coupon usage.
- Identify high-risk segments and patterns to inform fraud prevention strategies.
- Provide actionable insights to reduce fraud incidence and financial losses.
- Deliver clear, concise visualisations for technical and non-technical stakeholders.

# Methodology Steps:
1. Business Understanding: Define objectives, understand fraud context, identify key metrics.
2. Data Understanding: Explore dataset, assess quality, identify relevant features.
3. Data Preparation: Clean, transform, and engineer features for analysis.
4. Exploratory Data Analysis (EDA): Analyze data distributions, correlations, and patterns.
5. Data Visualisation: Create plots and dashboards to communicate findings.
6. Insights & Recommendations: Summarize findings, propose fraud mitigation strategies.

#





