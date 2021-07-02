import unittest
import csv

class Test(unittest.TestCase):

    def test_write_csv_file(self):
        myData = [["karthiq", "BE", "Mechanical"], ['Raj', 'BTech', 'Computers']]
        myFile = open('csv-write-data.csv', 'w')
        with myFile:
           writer = csv.writer(myFile)
           writer.writerows(myData)

if __name__ == "__main__":
    unittest.main()