age = 0

def age_check(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    


df = pd.read_csv("employee.csv")
df["salary"].dropna(inplace=True)

df.query("Select employee_name, Salary from employee Order by Salary DESC;")