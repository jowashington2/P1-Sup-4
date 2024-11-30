import unittest
from src.functions import next_ten_numbers, list_to_comma_string, write_to_csv
import os

class TestFunctions(unittest.TestCase):

    def test_next_ten_numbers(self):
        self.assertEqual(next_ten_numbers(5), "6,7,8,9,10,11,12,13,14,15")
        self.assertEqual(next_ten_numbers(-3), "-2,-1,0,1,2,3,4,5,6,7")

    def test_list_to_comma_string(self):
        self.assertEqual(list_to_comma_string(["apple", "banana", "cherry"]), "apple,banana,cherry")
        self.assertEqual(list_to_comma_string([]), "")

    def test_write_to_csv(self):
        headers = "Column1,Column2,Column3"
        data = "6,7,8,9,10,11,12,13,14,15"
        write_to_csv("test.csv", headers, data)

        with open("test.csv", "r") as file:
            lines = file.readlines()
            self.assertEqual(lines[0].strip(), headers)
            self.assertEqual(lines[1].strip(), data)

        # Clean up
        os.remove("test.csv")

if __name__ == '__main__':
    unittest.main()

