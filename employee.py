class Employee():
    def __init__(self,first_name,last_name,income):
        self.first_name=first_name
        self.last_name=last_name
        self.income=income

    def give_raise(self,num=5000):
        self.income+=num

import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        first_name="ada"
        last_name="wang"
        income=1000
        self.my_employee=Employee(first_name,last_name,income)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.give_raise(),6000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(3000)
        self.assertEqual(self.my_employee.give_raise(), 4000)

unittest.main()