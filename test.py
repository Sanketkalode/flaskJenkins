import unittest

from app import app


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        self.app_context.pop()

    def test_app(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_case(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
