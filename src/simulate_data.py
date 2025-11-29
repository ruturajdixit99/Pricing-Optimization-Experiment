import numpy as np
import pandas as pd


def simulate_experiment(n_users: int = 5000, seed: int = 42) -> pd.DataFrame:
    np.random.seed(seed)

    user_ids = np.arange(1, n_users + 1)

    # Randomly assign to control (A) or treatment (B)
    treatment_group = np.random.choice(["A", "B"], size=n_users, p=[0.5, 0.5])

    # Baseline price & engagement sensitivity
    base_price_A = 10.0
    base_price_B = 11.5  # higher price in treatment

    base_click_prob = 0.40
    base_conv_prob = 0.10

    # User heterogeneity: some users are more price sensitive
    price_sensitivity = np.random.normal(loc=0.0, scale=0.3, size=n_users)

    displayed_price = np.where(treatment_group == "A", base_price_A, base_price_B)

    # Adjust click and conversion probabilities by price sensitivity & price level
    price_delta = (displayed_price - base_price_A) / base_price_A

    click_prob = base_click_prob - 0.30 * price_delta + price_sensitivity
    conv_prob = base_conv_prob - 0.25 * price_delta + 0.5 * price_sensitivity

    # Clip to [0, 1]
    click_prob = np.clip(click_prob, 0.01, 0.95)
    conv_prob = np.clip(conv_prob, 0.01, 0.70)

    clicked = np.random.binomial(1, click_prob)
    purchased = np.random.binomial(1, conv_prob * clicked)  # can only buy if clicked

    revenue = purchased * displayed_price

    df = pd.DataFrame({
        "user_id": user_ids,
        "treatment_group": treatment_group,
        "displayed_price": displayed_price,
        "clicked": clicked,
        "purchased": purchased,
        "revenue": revenue
    })

    return df


if __name__ == "__main__":
    df = simulate_experiment()
    df.to_csv("D:\Projects\Finance\pricing_optimization_experiment\data\pricing_experiment_simulated.csv", index=False)
    print(df.head())
