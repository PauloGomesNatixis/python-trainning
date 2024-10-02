import unittest

from demo_tests import Cat


# setUpClass -> setUp -> test_meow -> tearDown -> setUp -> test_meow_2 -> tearDown... -> tearDownClass
class TestMeow(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat(name="test", status="neutral")

    def test_meow(self):
        result = self.cat.meow()
        expected_result = "The cat test says 'meow'!"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
