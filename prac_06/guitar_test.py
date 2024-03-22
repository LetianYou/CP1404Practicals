import unittest
from guitar import Guitar


class TestGuitarMethods(unittest.TestCase):

    def test_get_age(self):
        """ Test the get age function"""
        guitar = Guitar("Fender Stratocaster", 2014, 765.4)
        self.assertEqual(guitar.get_age(), 10)

    def test_is_vintage(self):
        """Test the is vintage function"""
        guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
        self.assertTrue(guitar.is_vintage())


unittest.main()
