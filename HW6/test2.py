from unittest import TestCase
import datetime
import HW6_Refactored

today = datetime.date.today()
d1 = datetime.date(2000, 1, 1)
d2 = datetime.date(2016, 10, 3)

class TestDiff_between_dates(TestCase):
    def test_dates_diff(self):
        self.assertLess(d1, today, str(d1) + " Provide date before current date")
        self.assertLess(d2, today, str(d2) + " Provide date before current date")

        self.assertEqual(HW6_Refactored.dates_difference(d1, d2), 6120)
        self.assertEqual(HW6_Refactored.dates_difference(d1, d2, 'D'), 6120)

        self.assertIsInstance(d1, datetime.date, "Type of arguments must be datetime.date")
        self.assertIsInstance(d2, datetime.date, "Type of arguments must be datetime.date")

        self.assertGreater(HW6_Refactored.dates_difference(d1, d2), 0, "Invalid Arguments")