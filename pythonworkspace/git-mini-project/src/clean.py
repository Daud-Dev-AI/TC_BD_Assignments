import pandas as pd
from pathlib import Path
import logging

BASE     = Path(__file__).parent.parent
TAX_RATE = 0.10   # 10 %

# Logging setup
LOG_FILE = BASE / "logs" / "clean.log"
LOG_FILE.parent.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# 1. Load CSV
logger.info("Loading CSV from '%s'", BASE / "data" / "sales_data.csv")
df = pd.read_csv(BASE / "data" / "sales_data.csv")
print(f"Loaded {len(df)} rows\n")
print(df.to_string(index=False))
print("Confliction")

# 2. Convert numeric
logger.info("Converting 'sales_amount' to numeric")
df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")

# 3. Remove invalid
invalid = df[df["sales_amount"].isna()]
if not invalid.empty:
    for _, row in invalid.iterrows():
        logger.warning(
            "Removing invalid row — order_id=%s, customer=%s, sales_amount=%r",
            row["order_id"], row["customer"], row["sales_amount"],
        )
    df = df.dropna(subset=["sales_amount"]).reset_index(drop=True)
    logger.info("Removed %d invalid row(s); %d rows remain", len(invalid), len(df))
else:
    logger.info("No invalid rows found")

# 4. Add tax
logger.info("Adding tax columns at rate %.0f%%", TAX_RATE * 100)
df["tax_amount"]     = (df["sales_amount"] * TAX_RATE).round(2)
df["total_with_tax"] = (df["sales_amount"] + df["tax_amount"]).round(2)

# 5. Save cleaned
output = BASE / "output" / "cleaned_sales_data.csv"
output.parent.mkdir(exist_ok=True)
df.to_csv(output, index=False)
logger.info("Cleaned data saved to '%s'", output)
