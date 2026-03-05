import pandas as pd
from pathlib import Path

BASE  = Path(__file__).parent.parent

# 1. Load cleaned CSV
dfsales = pd.read_csv(BASE / "output" / "cleaned_sales_data.csv")
print(f"Loaded {len(dfsales)} rows\n")

# 2. Group by Region and sum sales
totalsalesperregion = dfsales.groupby("region")["sales_amount"].sum().reset_index(name="total_sales").sort_values(by="total_sales", ascending=False)
print(totalsalesperregion)
print("\n")

# 3. Compute the total and average sales
totalsales = dfsales["sales_amount"].sum()
averagesales = dfsales["sales_amount"].mean()
print(f"Total Sales: {totalsales:.2f}")
print(f"Average Sales: {averagesales:.2f}")

# 4. Save summary
output = BASE / "output" / "sales_summary.csv"
output.parent.mkdir(exist_ok=True)
totalsalesperregion.to_csv(output, index=False)
print(f"\nSummary saved to '{output}'")