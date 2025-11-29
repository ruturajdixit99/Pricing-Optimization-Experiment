import numpy as np
import pandas as pd
from scipy import stats


def ab_summary(df: pd.DataFrame, group_col="treatment_group"):
    summary = (
        df.groupby(group_col)
        .agg(
            n_users=("user_id", "nunique"),
            clicks=("clicked", "sum"),
            purchases=("purchased", "sum"),
            revenue=("revenue", "sum")
        )
    )

    summary["ctr"] = summary["clicks"] / summary["n_users"]
    summary["cr"] = summary["purchases"] / summary["clicks"].clip(lower=1)
    summary["arpuc"] = summary["revenue"] / summary["n_users"]
    return summary


def two_proportion_ztest(success_a, total_a, success_b, total_b):
    p1 = success_a / total_a
    p2 = success_b / total_b
    p_pool = (success_a + success_b) / (total_a + total_b)
    se = np.sqrt(p_pool * (1 - p_pool) * (1 / total_a + 1 / total_b))
    z = (p2 - p1) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value


if __name__ == "__main__":
    df = pd.read_csv("D:\Projects\Finance\pricing_optimization_experiment\data\pricing_experiment_simulated.csv")
    summary = ab_summary(df)
    print("\n==== A/B SUMMARY ====")
    print(summary)

    a = summary.loc["A"]
    b = summary.loc["B"]

    # Conversion rate on purchases per user
    success_a = a["purchases"]
    total_a = a["n_users"]
    success_b = b["purchases"]
    total_b = b["n_users"]

    z, p = two_proportion_ztest(success_a, total_a, success_b, total_b)
    lift = (success_b / total_b) / (success_a / total_a) - 1

    print("\n==== PURCHASE CONVERSION LIFT (B vs A) ====")
    print(f"Lift: {lift * 100:.2f}%")
    print(f"z-score: {z:.3f}, p-value: {p:.5f}")
