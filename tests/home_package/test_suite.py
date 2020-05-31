import unittest
from tests.courses.read_from_csv_tests import ReadFromCSVTests
from tests.home_package.login_tests import LoginTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ReadFromCSVTests)

smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)