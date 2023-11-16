import unittest
import calc

class Testcalc(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calc.add(5, 5), 10)
    self.assertEqual(calc.add(20, 30), 50)
    self.assertEqual(calc.add(40, 60), 100)

  def test_subtract(self):
    self.assertEqual(calc.subtract(5, 5), 0)
    self.assertEqual(calc.subtract(7, 3), 4)
    self.assertEqual(calc.subtract(4, 1), 3)
    
  def test_multi(self):
    self.assertEqual(calc.multi(5, 4), 20)
    self.assertEqual(calc.multi(7, 5), 35)
    self.assertEqual(calc.multi(100, 5), 500)
    
  def test_div(self):
    self.assertEqual(calc.div(25, 5), 5)
    self.assertEqual(calc.div(50, 5), 10)
    self.assertEqual(calc.div(60, 5), 12)
    self.assertEqual(calc.div(5, 2), 2.5)
    
    
    with self.assertRaises(ValueError):
      calc.div(10, 0)

if __name__ == '__main__':
  unittest.main()