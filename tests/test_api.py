import unittest
from api import get_joke

class TestApi(unittest.TestCase):
    def test_get_joke(self):
        error = False
        
        try:
            actual = get_joke()
        except:
            error = True
        
        self.assertFalse(error)
        self.assertEqual(actual[0], 200)
        self.assertIsInstance(actual[1], dict)