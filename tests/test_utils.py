import unittest
from src.utils import validate_employees

class TestUtils(unittest.TestCase):

    def test_valid_employees(self):
        """Test valid employees data"""
        employees = [
            {"Employee_Name": "Alice", "Employee_EmailID": "alice@acme.com"},
            {"Employee_Name": "Bob", "Employee_EmailID": "bob@acme.com"}
        ]
        try:
            validate_employees(employees)  # Should not raise an error
        except Exception as e:
            self.fail(f"validate_employees() raised {e} unexpectedly!")

    def test_empty_employee_list(self):
        """Test that an error is raised for an empty employee list"""
        with self.assertRaises(ValueError):
            validate_employees([])

    def test_missing_email(self):
        """Test missing email field"""
        with self.assertRaises(ValueError):
            validate_employees([{"Employee_Name": "Alice"}])

    def test_missing_name(self):
        """Test missing name field"""
        with self.assertRaises(ValueError):
            validate_employees([{"Employee_EmailID": "alice@acme.com"}])

if __name__ == "__main__":
    unittest.main()
