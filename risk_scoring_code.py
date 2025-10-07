# 🎯 TRANSACTION RISK SCORING SYSTEM
# Based on patterns discovered in our EDA analysis

def calculate_risk_score(row):
    """
    Calculate risk score based on fraud patterns discovered in EDA
    Returns score from 0-100 (higher = more risky)
    """
    risk_score = 0
    
    # 1. COUNTRY RISK (0-25 points)
    country_risk = {
        'in': 25,    # 9.26% fraud rate - highest risk
        'br': 20,    # 7.45% fraud rate
        'jp': 18,    # 6.85% fraud rate  
        'de': 18,    # 6.79% fraud rate
        'au': 17,    # 6.37% fraud rate
        'uk': 17,    # 6.35% fraud rate
        'us': 15,    # 5.64% fraud rate
        'es': 14,    # 5.39% fraud rate
        'fr': 13,    # 5.19% fraud rate
        'ca': 11     # 4.33% fraud rate - lowest risk
    }
    risk_score += country_risk.get(row['country'], 12)  # default medium risk
    
    # 2. CHANNEL RISK (0-20 points)
    channel_risk = {
        'email': 20,   # 7.50% fraud rate - highest risk
        'ads': 19,     # 7.45% fraud rate
        'social': 16,  # 6.32% fraud rate
        'web': 16,     # 6.31% fraud rate
        'app': 15      # 6.15% fraud rate - lowest risk
    }
    risk_score += channel_risk.get(row['channel'], 16)  # default medium risk
    
    # 3. DEVICE RISK (0-15 points)
    device_risk = {
        'mobile': 15,   # 6.89% fraud rate - highest risk
        'desktop': 13,  # 5.99% fraud rate
        'tablet': 10    # 5.02% fraud rate - lowest risk
    }
    risk_score += device_risk.get(row['device'], 13)  # default medium risk
    
    # 4. AMOUNT RISK (0-20 points)
    # Based on our analysis: fraud avg = ~180, legit avg = ~85
    amount = row['amount']
    if amount > 300:        # Very high amount
        risk_score += 20
    elif amount > 200:      # High amount
        risk_score += 16
    elif amount > 150:      # Above fraud average
        risk_score += 12
    elif amount > 100:      # Above legit average
        risk_score += 8
    elif amount > 50:       # Medium amount
        risk_score += 4
    else:                   # Low amount
        risk_score += 2
    
    # 5. TIME RISK (0-10 points)
    # Night transactions might be riskier
    hour = row['hour']
    if 0 <= hour <= 5:      # Night (00:00-05:59)
        risk_score += 10
    elif 6 <= hour <= 11:   # Morning (06:00-11:59)
        risk_score += 3
    elif 12 <= hour <= 17:  # Afternoon (12:00-17:59)
        risk_score += 2
    else:                   # Evening (18:00-23:59)
        risk_score += 5
    
    # 6. OTHER FACTORS (0-10 points)
    # High number of items might be riskier
    if row['num_items'] > 4:
        risk_score += 6
    elif row['num_items'] > 2:
        risk_score += 3
    else:
        risk_score += 1
        
    # Coupon usage (might indicate legitimate behavior)
    if row['coupon_applied']:
        risk_score -= 2  # Slight reduction for coupon usage
    
    return min(risk_score, 100)  # Cap at 100

# Apply risk scoring to all transactions
print("🎯 Calculating Risk Scores for All Transactions...")
df['risk_score'] = df.apply(calculate_risk_score, axis=1)

# Define risk categories
def categorize_risk(score):
    if score >= 70:
        return 'HIGH'
    elif score >= 50:
        return 'MEDIUM'
    else:
        return 'LOW'

df['risk_category'] = df['risk_score'].apply(categorize_risk)

# Summary of risk scoring results
print("\n📊 RISK SCORING RESULTS")
print("=" * 50)

# Risk category distribution
risk_distribution = df['risk_category'].value_counts()
risk_pct = df['risk_category'].value_counts(normalize=True) * 100

print("\n1. Risk Category Distribution:")
for category in ['HIGH', 'MEDIUM', 'LOW']:
    count = risk_distribution.get(category, 0)
    pct = risk_pct.get(category, 0)
    print(f"   {category}: {count:,} transactions ({pct:.1f}%)")

# Risk score statistics
print(f"\n2. Risk Score Statistics:")
print(f"   Average Risk Score: {df['risk_score'].mean():.1f}")
print(f"   Median Risk Score: {df['risk_score'].median():.1f}")
print(f"   Min Risk Score: {df['risk_score'].min()}")
print(f"   Max Risk Score: {df['risk_score'].max()}")

# Fraud detection effectiveness
print(f"\n3. Fraud Detection Effectiveness:")
fraud_in_high = df[(df['risk_category'] == 'HIGH') & (df['is_fraud'] == True)].shape[0]
total_high = df[df['risk_category'] == 'HIGH'].shape[0]
total_fraud = df[df['is_fraud'] == True].shape[0]

if total_high > 0:
    precision = (fraud_in_high / total_high) * 100
    recall = (fraud_in_high / total_fraud) * 100
    print(f"   HIGH Risk Precision: {precision:.1f}% ({fraud_in_high}/{total_high} high-risk are fraud)")
    print(f"   HIGH Risk Recall: {recall:.1f}% ({fraud_in_high}/{total_fraud} frauds caught in high-risk)")

# Top 10 highest risk transactions (examples)
print(f"\n4. Top 10 Highest Risk Transactions:")
high_risk_examples = df.nlargest(10, 'risk_score')[['transaction_id', 'country', 'channel', 'device', 'amount', 'risk_score', 'risk_category', 'is_fraud']]
display(high_risk_examples)

print(f"\n5. Risk Score Breakdown by Actual Fraud Status:")
fraud_risk_analysis = df.groupby(['is_fraud', 'risk_category']).size().unstack(fill_value=0)
fraud_risk_pct = df.groupby(['is_fraud', 'risk_category']).size().unstack(fill_value=0)
fraud_risk_pct = fraud_risk_pct.div(fraud_risk_pct.sum(axis=1), axis=0) * 100
fraud_risk_pct = fraud_risk_pct.round(1)

print("\nCounts:")
display(fraud_risk_analysis)
print("\nPercentages:")
display(fraud_risk_pct)

# Save risk scores for future use
from pathlib import Path

# Create a summary table for reporting
risk_summary = df[['transaction_id', 'country', 'channel', 'device', 'amount', 
                   'num_items', 'coupon_applied', 'is_fraud', 'risk_score', 'risk_category']].copy()

# Save to CSV file in reports/tables directory
output_path = Path("reports/tables/transaction_risk_scores.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

risk_summary.to_csv(output_path, index=False)
print(f"✅ Risk scores saved to: {output_path}")

# Quick validation of saved file
saved_df = pd.read_csv(output_path)
print(f"📁 Saved file contains {len(saved_df):,} transactions with risk scores")

# Final summary
print(f"\n🎉 RISK SCORING SYSTEM COMPLETE!")
print(f"📈 Successfully scored {len(df):,} transactions")
print(f"🔍 Identified {len(df[df['risk_category'] == 'HIGH']):,} HIGH risk transactions")
print(f"⚠️  Identified {len(df[df['risk_category'] == 'MEDIUM']):,} MEDIUM risk transactions") 
print(f"✅ Identified {len(df[df['risk_category'] == 'LOW']):,} LOW risk transactions")

if total_high > 0:
    print(f"🎯 HIGH risk category captures {recall:.1f}% of all fraud cases")
    print(f"⚡ {precision:.1f}% of HIGH risk transactions are actually fraudulent")