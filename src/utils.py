import re
from typing import List, Dict

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def validate_employees(employees: List[Dict[str, str]]):
    """
    Validates the employee data ensuring:
    - No empty list
    - No missing or empty names
    - All email addresses are valid
    - No duplicate emails
    """
    if not employees:
        raise ValueError("No employees provided in the input file.")

    seen_emails = set()

    for idx, employee in enumerate(employees, start=1):
        name = employee.get("Employee_Name", "").strip()
        email = employee.get("Employee_EmailID", "").strip()

        if not name:
            raise ValueError(f"Employee at row {idx} has an empty or missing name.")

        if not email or not re.match(EMAIL_REGEX, email):
            raise ValueError(f"Invalid email format at row {idx}: '{email}'")

        if email in seen_emails:
            raise ValueError(f"Duplicate email found at row {idx}: '{email}'")
        
        seen_emails.add(email)
