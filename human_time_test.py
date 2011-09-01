import unittest
import human_time
from datetime import datetime


class KnownValues(unittest.TestCase):
    known_values = ((datetime(2011, 9, 1, 1, 2), "one o'clock"),
                    (datetime(2011, 9, 1, 1, 4), "five past one"),
                    (datetime(2011, 9, 1, 2, 12), "nearly quarter past two"),
                    (datetime(2011, 9, 1, 14, 12), "nearly quarter past two"),
                    (datetime(2011, 9, 1, 3, 17), "quarter past three"),
                    (datetime(2011, 9, 1, 15, 25), "nearly half past three"),
                    (datetime(2011, 9, 1, 4, 26), "half past four"),
                    (datetime(2011, 9, 1, 16, 33), "half past four"),
                    (datetime(2011, 9, 1, 5, 35), "twenty to six"),
                    (datetime(2011, 9, 1, 17, 36), "twenty to six"),
                    (datetime(2011, 9, 1, 8, 45), "quarter to nine"),
                    (datetime(2011, 9, 1, 20, 45), "quarter to nine"),
                    (datetime(2011, 9, 1, 9, 46), "quarter to ten"),
                    (datetime(2011, 9, 1, 21, 46), "quarter to ten"),
                    (datetime(2011, 9, 1, 10, 50), "five to eleven"),
                    (datetime(2011, 9, 1, 22, 50), "five to eleven"),
                    (datetime(2011, 9, 1, 23, 50), "five to midnight"),
                    (datetime(2011, 9, 1, 11, 50), "five to twelve"),
                    (datetime(2011, 9, 1, 12, 30), "half past twelve"),
                    (datetime(2011, 9, 1, 23, 58), "midnight"),
                    (datetime(2011, 9, 1, 0, 2), "midnight"),
                    (datetime(2011, 9, 1, 11, 58), "noon"),
    )
    
    def testKnownValues(self):
        for datetime_obj, human_str in self.known_values:
            result = human_time.human_time(datetime_obj)
            self.assertEqual(human_str, result)


if __name__ == "__main__":
    unittest.main()