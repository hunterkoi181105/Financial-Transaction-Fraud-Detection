# Financial-Transaction-Fraud-Detection
Machine Learning 251 HCMUT - ML in the hud

## Dataset
URL: https://www.kaggle.com/datasets/aryan208/financial-transactions-dataset-for-fraud-detection

## Download dataset
```bash
python download_dataset.py
```

## Overview
We use an open-source dataset from Kaggle with a usability of 10.0 and has thousands of downloading about financial transaction fraud detection. It has 18 features which include in a legitimate or fraudulent financial transaction. Overview, this dataset is fairly suitable for a basic Machine Learning project but still has some faults such as large amount of null data, data imbalance, etc. which can handle by data processing and featuring engineering. 

**Dataset Description**
- **Size**: ~5,000,000 transaction records
- **Nature**: Fully synthetic for privacy-safe analysis
- **Purpose**: Suitable for training and testing fraud detection models
- 
A structure of a transaction contains these fields:
- Transaction Details: ID, timestamp, sender/receiver accounts, amount, type (deposit, transfer, etc.)
- Behavioral Features: time since last transaction, spending deviation score, velocity score, geo-anomaly score
- Metadata: location, device used, payment channel, IP address, device hash
- Fraud Indicators: binary fraud label (is_fraud) and type of fraud (e.g., money laundering, account takeover)

## Model Selection
Our goal is to detect whether a financial transaction is legitimate or fradulent so that financial enterprise and organization such as bank, fund, etc. can avoid false transaction, report to authorities for legal action,... We choose 3 Machine Learning models for this problem:
1. Random Forest
2. XGBoost
3. Isolation Forest
