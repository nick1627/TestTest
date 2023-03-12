import unittest
from unittest.mock import patch
from employee import Employee

# test driven development = make test before you write code
# pyTest module also exists, but it's not the default like unittest.

class TestEmployee(unittest.TestCase):

    @classmethod #method for class, not for object
    def setUpClass(cls):
        # runs once before all tests
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        # runs once after all tests
        print("tearDownClass")

    def setUp(self): #specific method name
        print("setUp")
        #these are created before every test in the class
        self.emp1 = Employee("Bob", "Bobson", 50000)
        self.emp2 = Employee("Brian", "Brianson", 60000)
        

    def tearDown(self): #specific method name
        print("tearDown\n")
        # could be used to provide a clean slate for next tests
        pass

    def test_email(self):
        print("test_email")

        self.assertEqual(self.emp1.email, "Bob.Bobson@email.com")
        self.assertEqual(self.emp2.email, "Brian.Brianson@email.com")

        self.emp1.first = "Derek"
        self.emp2.first = "Terry"

        self.assertEqual(self.emp1.email, "Derek.Bobson@email.com")
        self.assertEqual(self.emp2.email, "Terry.Brianson@email.com")


    def test_fullname(self):
        print("test_fullname")

        self.assertEqual(self.emp1.fullname, "Bob Bobson")
        self.assertEqual(self.emp2.fullname, "Brian Brianson")

        self.emp1.first = "Derek"
        self.emp2.first = "Terry"

        self.assertEqual(self.emp1.fullname, "Derek Bobson")
        self.assertEqual(self.emp2.fullname, "Terry Brianson")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self):
        print("test_monthly_schedule")
        #here we will use mocking, because we want to run a test involving a response
        # from a website.  Whether or not the website runs is out of our control, so
        # we insert fake responses.
        with patch("employee.requests.get") as mocked_get: # use patch as context manager
            # the code employee.requests.get is replaced with mocked_get,
            # which has the following values
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            #now within the context manager, we run the test
            # must be inside this manager, so that the code is replaced
            # as required.
            schedule = self.emp1.monthly_schedule("May")
            #check method was called with correct URL
            mocked_get.assert_called_with("http://company.com/Bobson/May")
            # now check it returned the correct text
            self.assertEqual(schedule, "Success")


            #finally test a failed response, same structure, but don't need response string
            mocked_get.return_value.ok = False
        
            schedule = self.emp2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Brianson/June")
            self.assertEqual(schedule, "Bad Response!")


# the code below means that you can run this test with "python3 test_employee.py" in the terminal
if __name__ == "__main__": #if module is run directly, run the below
    unittest.main() # this will run all the methods starting with "test_"