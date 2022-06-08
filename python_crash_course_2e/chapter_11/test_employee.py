# test_employee.py

import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Test for the class Employee"""
    desf setUp(self):
        """
        Create an employee record for use in all test methods.
        """
        self.my_employee = Employee('elvis','presley',39_000_000)

    def test_give_default_raise(self):
        """Test that the default raise functions properly."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary,39_000_000+5_000)

    def test_give_custom_raise(self):
        """Test that the custom raise functions properly."""
        self.my_employee.give_raise(10_000)
        self.assertEqual(self.my_employee.annual_salary,39_000_000+10_000)

if __name__ == '__main__':
       unittest.main()


