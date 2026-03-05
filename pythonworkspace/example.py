import logging

a = [1,2,3]
b = a.copy()    # Creates a copy of the list, not a copy of the reference variable.
b.append(5)
b.pop()         # Removes last item in list
a.extend(b)     # Adds contents of b into tail of a
a.sort()        # Sorts in ascending order (in case of Strings, alphabetical order)
a.remove(2)     # Removes specific item or specific index

# data = ["100", "200", "abc", "300", ""]
# data = [item for item in data if item.isalpha() or item == ""]
# print(data)

order_id = 2
customer_id = 210
total_amount = 92109
mytuple = (order_id, customer_id, total_amount)
o_id, c_id, t_amt = mytuple
# print(f"Order number {o_id} for the customer {c_id} worth ${t_amt}")

exampleset = {"lint", "mean", "white", "wheeze", "nice", "lint"}

transaction_id = ["200", "300", "400", "190", "400", "300", "500"]
newset = set(transaction_id)
for i in newset:
    if i == "500":
        print("found")
    else:
        print("Not found")
newset.add("500")
print(newset)

tryl = [[5,4,3], 5, 6]
trys = ({5,2,3}, 6, [5,2,3])
trys[2].append(6)

row = {"name":"Tom", "age":"", "salary":"-4000"}

row["salary"] = float(row["salary"])
row["salary"] = int(row["salary"])
# row["age"] = None
row.update({"processed": True})
print(row)

def clean_row(row):
    name = row["name"].strip()
    age = int(row["age"]) if row["age"] != "" else 21
    salary = float(row["salary"]) if row["salary"] else 0

    return {
        "name" : name,
        "age" : age,
        "salary" : salary
    }
row = clean_row(row)
print(row)

def validate_row(row):
    if (isinstance(row["age"], int) and row["age"] >=0):
        if row["salary"] < 0:
            raise Exception("Salary cannot be negative")
        else:
            return True
    else:
        return False
try:
    kekw = validate_row(row)
    print(kekw)
except Exception as e:
    print("Handled Error")
data = "some data"
try:
    value = int(data)
except NameError:
    print("Value is not defined")
except ValueError:
    print("Invalid value")

logging.basicConfig(filename="example.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s") 

total_rows = 0
valid_rows = 0
invalid_rows = 0

rows = [
    {"name":"Tom", "age":"23", "salary":"-4000"},
    {"name":"Jerry", "age":"30", "salary":"5000"},
    {"name":"Spike", "age":"-5", "salary":"3000"}
]

for row_ in rows:
    total_rows += 1
    try:
        cleaned_row = clean_row(row_)
        if validate_row(cleaned_row):
            valid_rows += 1
        else:
            invalid_rows += 1
    except Exception as e:
        logging.error(f"Error processing row: {e}")
        invalid_rows += 1

logging.info("Data processing completed.")
logging.info(f"Total rows: {total_rows}, Valid rows: {valid_rows}, Invalid rows: {invalid_rows}")