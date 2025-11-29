# 📊 Pricing Optimization Experiment  
*A/B Testing, Revenue Impact & Causal Inference for Price Sensitivity Analysis*

---

## 🚀 Project Overview
This project simulates and analyzes the impact of pricing changes on user engagement, conversion, and revenue using **A/B Testing** and **Causal Inference** techniques.

Users are randomly assigned to:
| Group | Displayed Price | Purpose |
|-------|------------------|---------|
| **A (Control)** | $10.0 | Baseline pricing |
| **B (Treatment)** | $11.5 | Higher price to test revenue gain vs conversion drop |

The goal is to determine whether increasing the price improves overall revenue **without significantly hurting user behavior** (clicks, purchases).

---

## 🛠 Tech Stack
- **Python**, NumPy, Pandas  
- **Scikit-learn** for logistic regression  
- **SciPy** for statistical testing  
- **A/B Testing (z-test)**  
- **Causal Inference via Logistic Regression**

---

## 📁 Project Structure
pricing_optimization_experiment/
│── data/
│ └── pricing_experiment_simulated.csv
│
│── src/
│ ├── simulate_data.py # Synthetic data generation
│ ├── ab_test_analysis.py # A/B statistical evaluation
│ └── causal_inference.py # Logistic regression for causal impact
│
│── README.md # Project documentation
│── requirements.txt # Python dependencies
│── outputs/ (optional) # Place for charts/reports if generated

yaml
Copy code

---

## 📦 Installation & Setup
git clone <repo-link>
cd pricing_optimization_experiment
pip install -r requirements.txt

yaml
Copy code

---

## 📈 1. Simulated Data Generation (`simulate_data.py`)
Realistic behavioral dataset based on:
✔️ Price sensitivity (randomly generated per user)  
✔️ Click probability affected by price level  
✔️ Purchases only if user clicked  
✔️ Revenue calculated dynamically  

```python
revenue = purchased × displayed_price
Output preview:

less
Copy code
user_id | group | price | clicked | purchased | revenue
1       | A     | 10.0  | 0       | 0         | 0.0
2       | B     | 11.5  | 1       | 0         | 0.0
📊 2. A/B Testing Results (ab_test_analysis.py)
Metric	Group A	Group B
Users	2500	2500
CTR (Click Rate)	40.64%	35.56%
CR (Conversion Rate)	19.29%	16.98%
Revenue	1960	1736.5
ARPUC	0.784	0.694

📉 Conversion Lift (B vs A)
makefile
Copy code
Lift: -22.96%
z-score: -2.504
p-value: 0.01227
📌 Statistically significant decrease in conversion and revenue for Group B.

🎯 3. Causal Inference (causal_inference.py)
Logistic Regression to identify key behavioral drivers.

📈 Model Performance
makefile
Copy code
AUC: 0.842
Feature Influence (Log-Odds)
Feature	Effect
clicked	+4.62 (strongest predictor of purchasing)
displayed_price	-0.052 (higher price reduces purchase probability)
treatment_flag (Group B)	-0.034 (slight negative impact)

🔍 Most critical insight:

User engagement (clicks) is far more important in driving purchases than raising price.

💡 Insights & Interpretations
Behavioral Insights
Observation	Interpretation
CTR and CR dropped in Group B	Price increase discouraged engagement
Revenue also dropped in Group B	Lost purchases not compensated by higher price
Model highlight: clicks >> price	Focus on engagement before pricing experiments

🧠 Business Recommendations
Strategy	Reason
Do not deploy higher price blindly	It significantly hurts conversions and revenue
Test incremental pricing tiers	Smaller changes may perform better
Use segmented/personalized pricing	Different users have different sensitivities
Optimize conversion funnel	Click behavior is the strongest purchase driver

🏁 Final Conclusion
Increasing price from $10 → $11.5 resulted in lower engagement, conversion, and revenue.
The experiment shows that user sensitivity to price is high, and revenue gains from higher price do not offset purchase loss.

Future work could include:
✔️ Multi-group A/B/C pricing
✔️ Bayesian A/B testing
✔️ Dynamic pricing models
✔️ Personalization using user features (RFM, demographics)
