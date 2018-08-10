import unittest
from Views import combine_names, submit


class Test_Views(unittest.TestCase):

    def setUp(self):
        self.first_name = "araali"
        self.second_name = "farooq"
        self.contact = "077-2585664"
        self.email = "araali@email.com"
        self.combined_names = "araali farooq"

    def test_combine_names(self):
        full_name = combine_names(self.first_name, self.second_name)
        self.assertEqual(self.combined_names, full_name)