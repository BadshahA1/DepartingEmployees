import datetime

# Sample employee data
employees = [
    {"name": "John Doe", "termination_date": datetime.datetime(2023, 10, 27)},
    {"name": "Jane Doe", "termination_date": None},  # Still employed
    {"name": "Peter Smith", "termination_date": datetime.datetime(2023, 9, 15)},
]

# Function to disable user accounts based on termination date
def disable_departed_accounts(employees):
    for employee in employees:
        if employee.get("termination_date"):
            # Simulate disabling the account (replace with actual script)
            print(f"Disabling account for {employee['name']}")

# Disable departed employee accounts
disable_departed_accounts(employees)
