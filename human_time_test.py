import unittest
import human_time
from datetime import datetime


class KnownValues(unittest.TestCase):
    known_values = ((datetime(2011, 9, 1, 1, 1), "one o'clock"),
                    (datetime(2011, 9, 1, 1, 4), "just after one"),
                    (datetime(2011, 9, 1, 2, 6), "five past two"),
                    (datetime(2011, 9, 1, 2, 9), "nearly ten past two"),
                    (datetime(2011, 9, 1, 3, 11), "ten past three"),
                    (datetime(2011, 9, 1, 3, 14), "nearly quarter past three"),
                    (datetime(2011, 9, 1, 4, 16), "quarter past four"),
                    (datetime(2011, 9, 1, 4, 19), "nearly twenty past four"),
                    (datetime(2011, 9, 1, 5, 21), "twenty past five"),
                    (datetime(2011, 9, 1, 5, 24), "nearly twenty five past five"),
                    (datetime(2011, 9, 1, 6, 26), "twenty five past six"),
                    (datetime(2011, 9, 1, 6, 27), "nearly half past six"),
                    (datetime(2011, 9, 1, 7, 33), "half past seven"),
                    (datetime(2011, 9, 1, 7, 36), "twenty five to eight"),
                    (datetime(2011, 9, 1, 8, 39), "nearly twenty to nine"),
                    (datetime(2011, 9, 1, 8, 41), "twenty to nine"),
                    (datetime(2011, 9, 1, 9, 44), "nearly quarter to ten"),
                    (datetime(2011, 9, 1, 9, 46), "quarter to ten"),
                    (datetime(2011, 9, 1, 10, 49), "nearly ten to eleven"),
                    (datetime(2011, 9, 1, 10, 51), "ten to eleven"),
                    (datetime(2011, 9, 1, 11, 54), "nearly five to twelve"),
                    (datetime(2011, 9, 1, 11, 56), "five to twelve"),
                    (datetime(2011, 9, 1, 12, 58), "nearly one"),
                    (datetime(2011, 9, 1, 12, 0), "noon"),
                    (datetime(2011, 9, 1, 13, 1), "one o'clock"),
                    (datetime(2011, 9, 1, 13, 4), "just after one"),
                    (datetime(2011, 9, 1, 14, 6), "five past two"),
                    (datetime(2011, 9, 1, 14, 9), "nearly ten past two"),
                    (datetime(2011, 9, 1, 15, 11), "ten past three"),
                    (datetime(2011, 9, 1, 15, 14), "nearly quarter past three"),
                    (datetime(2011, 9, 1, 16, 16), "quarter past four"),
                    (datetime(2011, 9, 1, 16, 19), "nearly twenty past four"),
                    (datetime(2011, 9, 1, 17, 21), "twenty past five"),
                    (datetime(2011, 9, 1, 17, 24), "nearly twenty five past five"),
                    (datetime(2011, 9, 1, 18, 26), "twenty five past six"),
                    (datetime(2011, 9, 1, 18, 27), "nearly half past six"),
                    (datetime(2011, 9, 1, 19, 33), "half past seven"),
                    (datetime(2011, 9, 1, 19, 36), "twenty five to eight"),
                    (datetime(2011, 9, 1, 20, 39), "nearly twenty to nine"),
                    (datetime(2011, 9, 1, 20, 41), "twenty to nine"),
                    (datetime(2011, 9, 1, 21, 44), "nearly quarter to ten"),
                    (datetime(2011, 9, 1, 21, 46), "quarter to ten"),
                    (datetime(2011, 9, 1, 22, 49), "nearly ten to eleven"),
                    (datetime(2011, 9, 1, 22, 51), "ten to eleven"),
                    (datetime(2011, 9, 1, 23, 54), "nearly five to midnight"),
                    (datetime(2011, 9, 1, 23, 56), "five to midnight"),
                    (datetime(2011, 9, 1, 0, 58), "nearly one"),
                    (datetime(2011, 9, 1, 0, 0), "midnight"),
    )
    
    def testKnownValues(self):
        for datetime_obj, human_str in self.known_values:
            result = human_time.human_time(datetime_obj)
            self.assertEqual(human_str, result)


if __name__ == "__main__":
    unittest.main()