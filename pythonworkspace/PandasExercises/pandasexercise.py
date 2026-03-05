import pandas as pd
import numpy as np

# ============================================================
# SALES DATA
# ============================================================
print("=======================Sales Data==================================")

print("\nQuestion 1.1 - Load Data")
sales = pd.read_csv("PandasExercises/sales_data.csv")
print(sales)

print("\nQuestion 1.2 - Validate Schema")
expected_columns = ["order_id", "customer", "region", "product", "category", "sales_amount", "order_date"]
missing_cols = [col for col in expected_columns if col not in sales.columns]
extra_cols = [col for col in sales.columns if col not in expected_columns]
print("Expected columns:", expected_columns)
print("Actual columns:", list(sales.columns))
print("Missing columns:", missing_cols if missing_cols else "None")
print("Extra columns:", extra_cols if extra_cols else "None")
print("Schema valid:", not missing_cols and not extra_cols)

print("\nQuestion 1.3 - Clean Missing Values (Convert sales_amount to Numeric, Fill Missing)")
sales["sales_amount"] = pd.to_numeric(sales["sales_amount"], errors="coerce")
print("Rows with NaN sales_amount (including 'abc' coerced to NaN):", sales["sales_amount"].isna().sum())
median_sales = sales["sales_amount"].median()
sales["sales_amount"] = sales["sales_amount"].fillna(median_sales)
print("Filled missing sales_amount with median:", median_sales)
sales["order_date"] = pd.to_datetime(sales["order_date"], errors="coerce")
print(sales[["order_id", "sales_amount", "order_date"]])

print("\nQuestion 1.4 - Remove Invalid Records")
invalid_rows = sales[sales["order_date"].isna()]
if not invalid_rows.empty:
    print("Dropping rows with invalid order_date:")
    print(invalid_rows)
    sales = sales.dropna(subset=["order_date"]).reset_index(drop=True)
else:
    print("No invalid records found.")
print("Rows remaining:", len(sales))

print("\nQuestion 1.5 - Add Computed Columns")
sales["discounted_amount"] = (sales["sales_amount"] * 0.9).round(2)
sales["order_year"] = sales["order_date"].dt.year
sales["order_month"] = sales["order_date"].dt.month
print(sales[["order_id", "sales_amount", "discounted_amount", "order_year", "order_month"]])

print("\nQuestion 1.6 - Group by Region")
by_region = sales.groupby("region")["sales_amount"].agg(total_revenue="sum", avg_revenue="mean", order_count="count").reset_index()
print(by_region.to_string(index=False))

print("\nQuestion 1.7 - Group by Product")
by_product = sales.groupby("product")["sales_amount"].agg(total_revenue="sum", order_count="count").reset_index()
print(by_product.to_string(index=False))

print("\nQuestion 1.8 - Group by Category")
by_category = sales.groupby("category")["sales_amount"].agg(total_revenue="sum", order_count="count").reset_index()
print(by_category.to_string(index=False))

print("\nQuestion 1.9 - Calculate Revenue per Region (Sorted by Highest Revenue)")
revenue_sorted = by_region.sort_values("total_revenue", ascending=False)
print(revenue_sorted.to_string(index=False))

print("\nQuestion 1.10 - Multi-level Groupby (Region + Category)")
multi_group = sales.groupby(["region", "category"])["sales_amount"].sum().reset_index()
multi_group = multi_group.rename(columns={"sales_amount": "total_revenue"}).sort_values("total_revenue", ascending=False)
print(multi_group.to_string(index=False))



# ============================================================
# EMPLOYEE DATA
# ============================================================
print("\n=======================Employee Data==================================")

emp = pd.read_csv("PandasExercises/employee_data.csv")
print(emp)

print("\nQuestion 2.1 - Handle Invalid Salary ('abc' -> NaN)")
emp["salary"] = pd.to_numeric(emp["salary"], errors="coerce")
print("Rows with invalid/missing salary:")
print(emp[emp["salary"].isna()][["employee_id", "name", "salary"]])

print("\nQuestion 2.2 - Replace Missing Salary with Department Median")
emp["salary"] = emp.groupby("department")["salary"].transform(lambda s: s.fillna(s.median()))
emp["salary"] = emp["salary"].fillna(emp["salary"].median())
print(emp[["employee_id", "name", "department", "salary"]])

print("\nQuestion 2.3 - Filter Salary > 6000")
high_salary = emp[emp["salary"] > 6000]
print(high_salary[["employee_id", "name", "department", "salary"]])

print("\nQuestion 2.4 - Parse joining_date")
emp["joining_date"] = pd.to_datetime(emp["joining_date"], errors="coerce")
print(emp[["employee_id", "name", "joining_date"]])
print("Rows with missing joining_date:", emp["joining_date"].isna().sum())

print("\nQuestion 2.5 - Group by Department")
by_dept = emp.groupby("department")["salary"].agg(headcount="count", avg_salary="mean").reset_index()
print(by_dept.to_string(index=False))

print("\nQuestion 2.6 - Calculate Total Payroll")
payroll = emp.groupby("department")["salary"].sum().reset_index()
payroll = payroll.rename(columns={"salary": "total_payroll"}).sort_values("total_payroll", ascending=False)
print(payroll.to_string(index=False))

print("\nQuestion 2.7 - Add Tax Column (20% flat rate)")
emp["tax"] = (emp["salary"] * 0.20).round(2)
emp["net_salary"] = (emp["salary"] - emp["tax"]).round(2)
print(emp[["employee_id", "name", "salary", "tax", "net_salary"]])

print("\nQuestion 2.8 - Identify High Earners (above department average)")
emp["dept_avg_salary"] = emp.groupby("department")["salary"].transform("mean")
high_earners = emp[emp["salary"] > emp["dept_avg_salary"]][["employee_id", "name", "department", "salary", "dept_avg_salary"]]
print(high_earners.to_string(index=False))


# ============================================================
# TRANSACTIONS DATA
# ============================================================
print("\n=======================Transactions Data==================================")

txn = pd.read_csv("PandasExercises/transactions_data.csv")
print(txn)

print("\nQuestion 3.1 - Remove Duplicate Transactions")
dupes = txn[txn.duplicated(subset=["customer_id", "region", "amount", "status"], keep=False)]
print("Duplicate rows found:")
print(dupes)
txn = txn.drop_duplicates(subset=["customer_id", "region", "amount", "status"], keep="first").reset_index(drop=True)
print("Rows after deduplication:", len(txn))

print("\nQuestion 3.2 - Handle Invalid Amount ('abc' -> NaN, fill with median)")
txn["amount"] = pd.to_numeric(txn["amount"], errors="coerce")
print("Rows with invalid/missing amount:")
print(txn[txn["amount"].isna()][["transaction_id", "customer_id", "amount", "status"]])
median_amt = txn["amount"].median()
txn["amount"] = txn["amount"].fillna(median_amt)
print("Filled missing amounts with median:", median_amt)
print(txn[["transaction_id", "customer_id", "amount", "status"]])

print("\nQuestion 3.3 - Filter Only Completed Transactions")
completed = txn[txn["status"] == "Completed"]
print(completed.to_string(index=False))

print("\nQuestion 3.4 - Total Revenue by Region (Completed)")
revenue_by_region = completed.groupby("region")["amount"].sum().reset_index()
revenue_by_region = revenue_by_region.rename(columns={"amount": "total_revenue"}).sort_values("total_revenue", ascending=False)
print(revenue_by_region.to_string(index=False))

print("\nQuestion 3.5 - Identify Top Customer (Highest Total Spend, Completed)")
top_customers = completed.groupby("customer_id")["amount"].sum().reset_index()
top_customers = top_customers.rename(columns={"amount": "total_spent"}).sort_values("total_spent", ascending=False)
print(top_customers.to_string(index=False))
print("Top customer:", top_customers.iloc[0]["customer_id"], "| Total spent:", top_customers.iloc[0]["total_spent"])

print("\nQuestion 3.6 - Count Failed Transactions")
failed = txn[txn["status"] == "Failed"]
print("Total failed transactions:", len(failed))
print(failed[["transaction_id", "customer_id", "region", "amount"]].to_string(index=False))
