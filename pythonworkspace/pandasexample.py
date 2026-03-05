import pandas as pd

# s = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])

# data = {
# 	"name": ["Alice", "Bob"],
# 	"age": [25, 30]
# }

# df = pd.read_csv(
#     "employees.csv",
#     sep=",",
#     dtype={"name": str, "age": int, "salary": float},
#     na_values=["", "NA", "N/A"],
#     parse_dates=["start_date"],
#     keep_default_na=False
# )

df = pd.read_csv("data.csv")
dfsales = pd.read_csv("sales_data.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())
print(df.isnull().sum().sum())
df = df[df['salary'] != 'abc']
# Drop rows if null in column 'A' or 'B'
df.dropna(subset=['salary'], inplace=True)
df['salary'] = df['salary'].astype('int64')
print(dfsales)
dfsales.dropna(subset=['sales_amount'], inplace=True)
dfsales = dfsales[dfsales["sales_amount"] != 'abc']
dfsales['sales_amount'] = dfsales['sales_amount'].astype('float64')
# print(df.query("age > 30 and salary > 5000"))
# print(df.query("(region == 'North') and (salary > 5000 and salary < 8000) and (name.str.startswith('A'))"))
# print("\n")

# Individually printing the filters for demonstration
# print(df.query("region == 'North'"))
# print("\n")
# print(df.query("salary > 5000 and salary < 8000"))
# print("\n")
# print(df.query("name.str.startswith('A')"))
df["bonus"] = df["salary"] * 0.10
df["tax"] = df["salary"] * 0.15
df["net_salary"] = df["salary"] + df["bonus"] - df["tax"]
df["flag"] = df["net_salary"].apply(lambda x: "High" if x > 6500 else "Low")
df = df.sort_values("net_salary", ascending=False)
df1 = df.agg({
    "salary": ["sum", "mean"],
    "age": ["min", "max"]
})
df2 = df.agg({
    "net_salary": ["std","mean"],
    "employee_id": ["count"]
})
# print(df)
# print(df2)
# print(df.head())

# result = df.groupby("region")["salary"].sum().reset_index(name="total_salary")
# print(result)

totalsalesperregion = dfsales.groupby("region")["sales_amount"].sum().reset_index(name="total_sales")
print(totalsalesperregion)
print("\n")
totalsalesperregionproduct = dfsales.groupby(["region", "product"])["sales_amount"].sum().reset_index(name="total_sales")
print(totalsalesperregionproduct)
print("\n")
topregionbyrevenue = dfsales.groupby("region")["sales_amount"].sum().reset_index(name="total_sales").sort_values("total_sales", ascending=False).head(1)
print(topregionbyrevenue)
