import unittest
from unittest.mock import MagicMock, patch
import builtins
from inputs import get_user_number

class TestInputs(unittest.TestCase):
    def test_get_user_number(self):
        with patch("builtins.input", return_value = "3") as input:
            actual = get_user_number()
            expectation = 3.0
            self.assertEqual(actual, expectation)
            self.assertEqual(input.call_count, 1)