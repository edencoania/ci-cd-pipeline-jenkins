import requests
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:1234/"
        response = requests.get(self.url)
        if 'application/json' in response.headers.get('content-type', ''):
            self.data = response.json()
        else:
            self.data = None

    def test_check(self):
        assert self.data is None

if __name__ == '__main__':
    unittest.main()

