import unittest
from task_01_duck_typing import Circle

class TestCircle(unittest.TestCase):
    def test_circle_negative(self):
        with self.assertRaises(ValueError) as context:
            Circle(radius=5)
        self.assertEqual(str(context.exception),"Radius cannot be negative")

if __name__ == "__main__":
    unittest.main()

