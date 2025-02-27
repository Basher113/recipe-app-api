from django.test import SimpleTestCase
from . import calc

class CalcTest(SimpleTestCase):
    """Test the calc module"""
    def test_calc_add(self):
        """Test adding numbers together."""
        sum = calc.add(5, 6)
        self.assertEqual(sum, 11)
        self.assertNotEqual(sum, 15)

    def test_calc_minus(self):
        """Test minus numbers together"""
        difference = calc.minus(6, 5)
        self.assertEqual(difference, 1)
        