import unittest
from src.secret_santa import SecretSanta

class TestSecretSanta(unittest.TestCase):
    
    def setUp(self):
        """Set up common test data"""
        self.employees = [
            {"Employee_Name": "Alice", "Employee_EmailID": "alice@acme.com"},
            {"Employee_Name": "Bob", "Employee_EmailID": "bob@acme.com"},
            {"Employee_Name": "Charlie", "Employee_EmailID": "charlie@acme.com"}
        ]

    def test_assign_secret_children(self):
        """Test basic Secret Santa assignment"""
        secret_santa = SecretSanta(self.employees)
        assignments = secret_santa.assign_secret_children()

        # Check that everyone gets exactly one assignment
        self.assertEqual(len(assignments), len(self.employees))

        # Ensure each person does not get themselves
        for assignment in assignments:
            self.assertNotEqual(assignment["Employee_EmailID"], assignment["Secret_Child_EmailID"])

        # Ensure all employees are assigned uniquely
        assigned_children = {a["Secret_Child_EmailID"] for a in assignments}
        self.assertEqual(len(assigned_children), len(self.employees))  # No duplicates

    def test_no_self_assignment(self):
        """Ensure no one is assigned to themselves"""
        secret_santa = SecretSanta(self.employees)
        assignments = secret_santa.assign_secret_children()
        for assignment in assignments:
            self.assertNotEqual(assignment["Employee_EmailID"], assignment["Secret_Child_EmailID"])

    def test_previous_assignments_exclusion(self):
        """Ensure that last year's assignments are not repeated"""
        previous_assignments = [
            {"Employee_Name": "Alice", "Employee_EmailID": "alice@acme.com", "Secret_Child_Name": "Bob", "Secret_Child_EmailID": "bob@acme.com"},
            {"Employee_Name": "Bob", "Employee_EmailID": "bob@acme.com", "Secret_Child_Name": "Charlie", "Secret_Child_EmailID": "charlie@acme.com"},
            {"Employee_Name": "Charlie", "Employee_EmailID": "charlie@acme.com", "Secret_Child_Name": "Alice", "Secret_Child_EmailID": "alice@acme.com"},
        ]
        
        secret_santa = SecretSanta(self.employees, previous_assignments)
        assignments = secret_santa.assign_secret_children()

        for assignment in assignments:
            last_year_child = next(
                (a["Secret_Child_EmailID"] for a in previous_assignments if a["Employee_EmailID"] == assignment["Employee_EmailID"]),
                None
            )
            self.assertNotEqual(assignment["Secret_Child_EmailID"], last_year_child)

    def test_single_employee_error(self):
        """Test that an error is raised when only one employee exists"""
        single_employee = [{"Employee_Name": "Alice", "Employee_EmailID": "alice@acme.com"}]
        secret_santa = SecretSanta(single_employee)

        with self.assertRaises(ValueError):
            secret_santa.assign_secret_children()

if __name__ == "__main__":
    unittest.main()
