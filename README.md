📊 Pricing Optimization Experiment

A/B Testing & Causal Inference for Revenue Optimization

🧠 Project Overview

This project simulates a pricing experiment where users are split into two groups:

Version	Price	Purpose
Group A (Control)	$10.0	Baseline pricing
Group B (Treatment)	$11.5	Higher price to test revenue impact

The goal is to evaluate the trade-off between higher pricing and user behavior — specifically, whether raising price leads to more or less revenue, considering user engagement, conversion rate, and price sensitivity.

🚀 Workflow & Components
1️⃣ Data Simulation (simulate_data.py)

A synthetic dataset of 5,000 users is generated with realistic behavioral patterns including:

Random assignment to A/B groups

Click probability influenced by price sensitivity

Purchases only if user clicked (conversion funnel logic)

Revenue generated as:

revenue = purchased × displayed_price


This creates variability in user behavior, mimicking real-world dynamics like discount effects, drop-offs, engagement, and purchase intention.

👉 Output sample:

user_id | group | price | clicked | purchased | revenue

2️⃣ Statistical A/B Test (ab_test_analysis.py)

We evaluate experiment results using:

CTR (Click-Through Rate)

CR (Conversion Rate)

ARPUC (Average Revenue Per User Click)

Lift in conversion rate

Statistical significance via Z-test

📌 Summary Results:

Metric	Group A	Group B
Users	2500	2500
CTR	40.64%	35.56%
Purchase Conversion (CR)	19.29%	16.98%
Revenue	1960	1736.5
ARPUC	0.784	0.694

📉 Conversion Lift (B vs A): -22.96%
📊 p-value: 0.01227 → Statistically significant difference

➡️ Interpretation:
Raising the price decreased purchase probability, clicks, and revenue. Even though treatment users faced higher price, it did not compensate for reduced engagement.

3️⃣ Causal Inference (causal_inference.py)

To understand why Group B underperformed, we used Logistic Regression to evaluate the causal impact of price and treatment on purchases.

📈 AUC = 0.842 → Good predictive power

📌 Feature Importance (purchase probability in log-odds):

Feature	Effect
clicked	+4.62 → Very strong influence (primary gateway to purchase)
displayed_price	-0.052 → Higher price reduces purchase likelihood
treatment_flag	-0.034 → Belonging to Treatment group slightly reduces buying tendency

🧠 Interpretation:

Clicking is the strongest trigger for purchase.

Higher price directly denies conversion.

Price increase has a stronger negative impact than any positive revenue benefit.

📚 Key Insights & Business Takeaways
🔍 Behavioral Insights:
Observation	Insight
Lower CTR & CR in Group B	Users react negatively to increased price
Revenue decreased for Group B	Higher price did not recover lost conversions
Treatment_flag had weak negative effect	Treatment change slightly discouraged purchases
Clicking outweighs pricing impact	Engagement is key driver of conversion
💼 Business Recommendations
Suggestion	Reasoning
Do not deploy higher pricing directly	Statistically significant drop in conversions and revenue
Consider discount tier testing	Test small incremental pricing instead of direct jump
Use personalized pricing (price elasticity model)	Different users have different price sensitivities
Prioritize conversion funnel optimization	"Clicked" is the most powerful purchase predictor
📁 Folder Structure
pricing_optimization_experiment/
│── data/
│   └── pricing_experiment_simulated.csv
│
│── src/
│   ├── simulate_data.py      → Generate synthetic behavioral dataset
│   ├── ab_test_analysis.py   → Perform A/B aggregation & statistical testing
│   └── causal_inference.py   → Understand causal drivers using logistic regression
│
│── outputs/   (optional, for reports and plots)
│── README.md
│── requirements.txt

🎯 Final Conclusion

Price Increase (Group B) = Higher cost but lower engagement → Net revenue loss.

Even though increasing price may seem beneficial, it reduced user willingness to engage and purchase, leading to a statistically significant negative lift of -22.96%.

In real-world deployment, maintaining lower price (A) or testing smaller price increments along with enhanced engagement would be more profitable.
