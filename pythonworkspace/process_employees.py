import csv
import logging

logging.basicConfig(filename="process_employees.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

INPUT_FILE  = "employees.csv"
OUTPUT_FILE = "employees_cleaned.csv"

metrics = {
    "total":           0,
    "valid":           0,
    "invalid_age":     0,
    "missing_salary":  0,
    "other_errors":    0,
}

def clean_row(row):
    name = row["name"].strip()
    if not name:
        raise ValueError("Empty name")
    raw_age = row["age"].strip()
    if not raw_age:
        raise ValueError(f"Missing age for '{name}'")
    try:
        age = int(raw_age)
    except ValueError:
        raise ValueError(f"Invalid age '{raw_age}' for '{name}'")
    if age < 0:
        raise ValueError(f"Negative age {age} for '{name}'")
    raw_salary = row["salary"].strip()
    if not raw_salary:
        salary = 0.0
        metrics["missing_salary"] += 1
        logging.warning(f"Missing salary for '{name}' — defaulting to 0")
    else:
        try:
            salary = float(raw_salary)
        except ValueError:
            raise ValueError(f"Invalid salary '{raw_salary}' for '{name}'")

    return {"name": name, "age": age, "salary": salary}

cleaned_rows = []

with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        metrics["total"] += 1
        try:
            cleaned = clean_row(row)
            cleaned_rows.append(cleaned)
            metrics["valid"] += 1

        except ValueError as e:
            error_msg = str(e)
            # Categorise the invalid row
            if "age" in error_msg.lower():
                metrics["invalid_age"] += 1
            else:
                metrics["other_errors"] += 1
            logging.warning(f"Skipping row {metrics['total']} — {error_msg} | raw={dict(row)}")

        except Exception as e:
            metrics["other_errors"] += 1
            logging.error(f"Unexpected error on row {metrics['total']}: {e} | raw={dict(row)}")
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
    fieldnames = ["name", "age", "salary"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

    
print("=" * 45)
print("  Data Processing Complete")
print("=" * 45)
print(f"  Total rows read      : {metrics['total']}")
print(f"  Valid rows written   : {metrics['valid']}")
print(f"  Skipped (bad age)   : {metrics['invalid_age']}")
print(f"  Salary defaulted to 0 : {metrics['missing_salary']}")
print(f"  Other errors        : {metrics['other_errors']}")
print("=" * 45)
print(f"  Cleaned file -> {OUTPUT_FILE}")
print(f"  Log file     -> process_employees.log")
print("=" * 45)

logging.info("=" * 45)
logging.info("Processing complete.")
logging.info(f"Total: {metrics['total']} | Valid: {metrics['valid']} | "
             f"Bad age: {metrics['invalid_age']} | Missing salary: {metrics['missing_salary']} | "
             f"Other errors: {metrics['other_errors']}")
