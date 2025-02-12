from src.secret_santa import SecretSanta
from pathlib import Path
from src.logger import get_logger

logger = get_logger(__name__)

DATA_DIR = Path("data")
EMPLOYEES_FILE = DATA_DIR / "employees.csv"
PREVIOUS_ASSIGNMENTS_FILE = DATA_DIR / "previous_assignments.csv"
OUTPUT_FILE = DATA_DIR / "assignments.csv"

def read_employee_data():
    """Reads employee data from CSV, ensuring the file exists."""
    if not EMPLOYEES_FILE.exists():
        logger.error(f"Employee file not found: {EMPLOYEES_FILE}")
        raise FileNotFoundError(f"Missing required file: {EMPLOYEES_FILE}")
    
    return SecretSanta.read_csv(EMPLOYEES_FILE)

def read_previous_assignments():
    """Reads previous year's Secret Santa assignments if available."""
    if PREVIOUS_ASSIGNMENTS_FILE.exists():
        return SecretSanta.read_csv(PREVIOUS_ASSIGNMENTS_FILE)
    return []

def write_output(assignments):
    """Writes the Secret Santa assignments to a CSV file."""
    DATA_DIR.mkdir(exist_ok=True)  # Ensure the output directory exists
    SecretSanta.write_assignments_to_csv(assignments, OUTPUT_FILE)
    logger.info(f"Assignments saved to {OUTPUT_FILE}")

def main():
    """Main function to run the Secret Santa assignment."""
    try:
        employees = read_employee_data()
        previous_assignments = read_previous_assignments()

        secret_santa = SecretSanta(employees, previous_assignments)
        assignments = secret_santa.assign_secret_children()

        write_output(assignments)
        logger.info("Secret Santa assignments generated successfully!")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
