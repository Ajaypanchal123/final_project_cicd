import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        tester = app.test_client(self)
        response = tester.get('/api/data')
        self.assertEqual(response.json, {"message": "Hello, CI/CD World!"})

if __name__ == "__main__":
    unittest.main()
