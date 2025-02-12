import random
import csv
from typing import List, Dict, Optional
from .utils import validate_employees
from .logger import get_logger

logger = get_logger(__name__)

class SecretSanta:
    MAX_RETRIES = 10  # Number of retries if valid assignments aren't found

    def __init__(self, employees: List[Dict[str, str]], previous_assignments: Optional[List[Dict[str, str]]] = None):
        """
        Initialize the SecretSanta class with employees and optional previous assignments.
        """
        self.employees = employees
        self.previous_assignments = previous_assignments or []
        self.assignments = []
        
        validate_employees(self.employees)  # Ensure data is valid
        self.previous_map = self._build_previous_assignment_map()
        logger.info("SecretSanta initialized with employees and previous assignments.")

    def _build_previous_assignment_map(self) -> Dict[str, str]:
        """Creates a mapping of employees to their previous year's secret child."""
        return {
            assignment["Employee_EmailID"]: assignment["Secret_Child_EmailID"]
            for assignment in self.previous_assignments
        }

    def _get_possible_children(self, employee_email: str, available_children: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Returns a list of valid secret children for a given employee.
        """
        previous_child = self.previous_map.get(employee_email)
        return [
            child for child in available_children
            if child["Employee_EmailID"] != employee_email and  # Cannot be self
               child["Employee_EmailID"] != previous_child  # Cannot be previous year's child
        ]

    def assign_secret_children(self) -> List[Dict[str, str]]:
        """
        Assign secret children to employees based on constraints.
        Retries assignment multiple times if no valid configuration is found.
        """
        for attempt in range(self.MAX_RETRIES):
            logger.info(f"Attempt {attempt + 1} to assign Secret Santa.")
            available_children = self.employees.copy()
            random.shuffle(available_children)
            temp_assignments = []
            failed = False

            for employee in self.employees:
                possible_children = self._get_possible_children(employee["Employee_EmailID"], available_children)

                if not possible_children:
                    logger.warning(f"No valid secret child found for {employee['Employee_Name']}. Retrying...")
                    failed = True
                    break  # Restart assignment process

                secret_child = random.choice(possible_children)
                temp_assignments.append({
                    "Employee_Name": employee["Employee_Name"],
                    "Employee_EmailID": employee["Employee_EmailID"],
                    "Secret_Child_Name": secret_child["Employee_Name"],
                    "Secret_Child_EmailID": secret_child["Employee_EmailID"]
                })
                available_children.remove(secret_child)  # Remove assigned child

            if not failed:
                self.assignments = temp_assignments
                logger.info("Secret Santa assignments completed successfully.")
                return self.assignments  # Successful assignment

        logger.error("Could not generate a valid Secret Santa assignment after multiple attempts.")
        raise ValueError("No valid Secret Santa assignment found after multiple retries.")

    @staticmethod
    def write_assignments_to_csv(assignments: List[Dict[str, str]], output_file: str):
        """
        Write assignments to a CSV file.
        """
        try:
            if not assignments:
                raise ValueError("No assignments provided for CSV export.")

            with open(output_file, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
                writer.writeheader()
                writer.writerows(assignments)
            logger.info(f"Assignments successfully written to {output_file}.")

        except Exception as e:
            logger.error(f"Error writing assignments to CSV: {e}")
            raise

    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, str]]:
        """
        Read a CSV file and return a list of dictionaries.
        """
        try:
            with open(file_path, mode="r", newline="") as file:
                data = list(csv.DictReader(file))

                if not data:
                    raise ValueError(f"CSV file {file_path} is empty.")

                return data

        except Exception as e:
            logger.error(f"Error reading CSV file {file_path}: {e}")
            raise
