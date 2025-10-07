# Synthetic E‑Commerce Transactions with Fraud Label

This is a **random, easy-to-use** synthetic dataset of e-commerce transactions suitable for **binary classification** (fraud detection) and general tabular ML tasks.

## Files
- `transactions.csv` — main dataset with 10,000 rows and 12 columns.
- `data_dictionary.csv` — column descriptions and types.

## Schema (quick view)
| column | type | description |
|---|---|---|
| transaction_id | int | Unique transaction identifier. |
| user_id | int | Anonymous user identifier. |
| timestamp | datetime | Transaction timestamp (UTC). |
| amount | float | Order amount in arbitrary currency units. |
| country | category | ISO-like country code (synthetic). |
| device | category | Access device used for the transaction. |
| channel | category | Acquisition channel for the transaction. |
| hour | int [0-23] | Hour of day derived from timestamp. |
| dayofweek | int [0=Mon ... 6=Sun] | Day of week derived from timestamp. |
| coupon_applied | binary {0,1} | Whether a coupon was applied to the order. |
| num_items | int | Number of items in the order (>=1). |
| is_fraud | binary {0,1} | Target label indicating fraudulent transaction. |

## Generation Notes
- Data is fully synthetic; no real users.
- Class imbalance is **moderate** (~few % fraud) and **feature-dependent** (night hours, higher amounts, certain channels/devices).
- Columns like `hour`, `dayofweek` are provided for convenience.

## Suggested Uses
- Fraud detection baselines (LogReg, XGBoost, LightGBM).
- Feature importance and interpretability exercises (SHAP).
- Class-imbalance techniques (SMOTE, class weights).
- EDA & visualization practice.

## Citation
If you use this dataset, please link back to the Kaggle dataset page once you publish.

## License
CC BY 4.0 (synthetic).
