from unittest import TestCase
import datetime

today = datetime.date.today()
d1 = datetime.date(2000, 1, 1)
d2 = datetime.date(2016, 10, 3)

class Test_dates(TestCase):

    def test_days_between_two_dates(self):
        self.assertLess(d1, today, str(d1) + " Provide date before current date")
        self.assertLess(d2, today, str(d2) + " Provide date before current date")

    def test_months_between_two_dates(self):
        self.assertIsInstance(d1, datetime.date, "Type of arguments must be datetime.date")
        self.assertIsInstance(d2, datetime.date, "Type of arguments must be datetime.date")

    def test_years_between_two_dates(self):
        diff = d1 - d2
        self.assertLess(diff.days, 0, "Invalid Arguments")