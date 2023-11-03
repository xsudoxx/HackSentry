import unittest
import sys
import os

# Include the path to the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Sentry import check_url

class TestRegex(unittest.TestCase):
    def test_valid_urls(self):
        self.assertTrue(check_url('http://www.example.com'))
        self.assertTrue(check_url('https://www.example.com'))
        self.assertTrue(check_url('http://example.com'))
        self.assertTrue(check_url('https://example.com'))
        self.assertTrue(check_url('http://subdomain.example.com'))
        self.assertTrue(check_url('http://www.example.co.uk'))
        self.assertTrue(check_url('http://192.168.1.1'))
        self.assertTrue(check_url('http://[2001:db8::1]'))
    
    def test_invalid_urls(self):
        self.assertFalse(check_url('htp://www.example.com'))
        self.assertFalse(check_url('example.com'))
        self.assertFalse(check_url('://www.example.com'))
        self.assertFalse(check_url('http://'))
        self.assertFalse(check_url('http://.com'))

if __name__ == "__main__":
    unittest.main()