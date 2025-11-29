import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report


if __name__ == "__main__":
    df = pd.read_csv("D:\Projects\Finance\pricing_optimization_experiment\data\pricing_experiment_simulated.csv")

    df["treatment_flag"] = (df["treatment_group"] == "B").astype(int)

    # Outcome: did user purchase?
    y = df["purchased"]

    # Features: treatment + price + basic engagement signal
    X = df[["treatment_flag", "displayed_price", "clicked"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("AUC:", roc_auc_score(y_test, y_prob))
    print("Classification report")
    print(classification_report(y_test, y_pred))

    coeffs = pd.DataFrame({
        "feature": X.columns,
        "coef": model.coef_[0]
    }).sort_values("coef", ascending=False)

    print("\n=== Treatment effect sign & magnitude (log-odds) ===")
    print(coeffs)
