import os
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "campus_cafe_sales.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA, parse_dates=["date"])
    df["revenue_gbp"] = df["units"] * df["unit_price_gbp"]

    print("\n=== Dataset ===")
    print(f"Rows: {len(df):,}")
    print(f"Date range: {df['date'].min().date()} to {df['date'].max().date()}")
    print("\n=== Revenue ===")
    print(f"Total revenue: £{df['revenue_gbp'].sum():,.2f}")
    print(f"Mean transaction revenue: £{df['revenue_gbp'].mean():.2f}")

    # 1) Daily revenue time series
    daily = df.groupby("date")["revenue_gbp"].sum().sort_index()
    plt.figure()
    daily.plot()
    plt.title("Daily revenue (GBP)")
    plt.xlabel("Date")
    plt.ylabel("Revenue (£)")
    plt.tight_layout()
    plt.savefig(OUT / "01_daily_revenue.png", dpi=150)
    plt.close()

    # 2) Revenue by outlet (bar)
    by_outlet = df.groupby("outlet")["revenue_gbp"].sum().sort_values(ascending=False)
    plt.figure()
    by_outlet.plot(kind="bar")
    plt.title("Revenue by outlet (GBP)")
    plt.xlabel("Outlet")
    plt.ylabel("Revenue (£)")
    plt.tight_layout()
    plt.savefig(OUT / "02_revenue_by_outlet.png", dpi=150)
    plt.close()

    # 3) Top 10 items by revenue
    top_items = df.groupby("item")["revenue_gbp"].sum().sort_values(ascending=False).head(10)
    plt.figure()
    top_items.sort_values().plot(kind="barh")
    plt.title("Top 10 items by revenue (GBP)")
    plt.xlabel("Revenue (£)")
    plt.ylabel("Item")
    plt.tight_layout()
    plt.savefig(OUT / "03_top_items.png", dpi=150)
    plt.close()

    # 4) Heatmap-style pivot (hour x category) using simple imshow
    pivot = df.pivot_table(index="hour", columns="category", values="revenue_gbp", aggfunc="sum").fillna(0)
    plt.figure()
    plt.imshow(pivot.values, aspect="auto")
    plt.title("Revenue by hour and category (GBP)")
    plt.xlabel("Category")
    plt.ylabel("Hour of day")
    plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=30, ha="right")
    plt.yticks(range(len(pivot.index)), pivot.index)
    plt.tight_layout()
    plt.savefig(OUT / "04_hour_category_heatmap.png", dpi=150)
    plt.close()

    print("\n✅ Done. Plots saved to: outputs/")
    for p in sorted(OUT.glob("*.png")):
        print(f" - {p.name}")

if __name__ == "__main__":
    main()
