import unittest
from validation import validate_email, validate_contact

class Test_Validation(unittest.TestCase):

    def setUp(self):
        self.valid_contact = "077-2854664"
        self.invalid_contact = "0772-2854664"
        self.valid_email = "araali@email.com"
        self.invalid_email = "araali.email.com"
    
    def test_invalid_contact(self):
        resp = validate_contact(self.invalid_contact)
        self.assertEqual(resp, False)

    def test_invalid_email(self):
        resp = validate_email(self.invalid_email)
        self.assertEqual(resp, False)  


    def test_valid_contact(self):
        resp = validate_contact(self.valid_contact)
        self.assertEqual(resp, True)

    def test_valid_email(self):
        resp = validate_email(self.valid_email)
        self.assertEqual(resp, True)    