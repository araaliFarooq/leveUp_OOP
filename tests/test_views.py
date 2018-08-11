import unittest
from ..Views import add_new_user, combine_names


class Test_Views(unittest.TestCase):

    def setUp(self):
        self.first_name = "araali"
        self.second_name = "farooq"
        self.contact = "077-2585664"
        self.email = "araali@email.com"
        self.combined_names = "araali farooq"
        self.all_users = [{"full_name":"araali farooq", "contact":"077-2585664", "email":"araali@email.com"}]

    def test_combine_names(self):
        full_name = combine_names(self.first_name, self.second_name)
        self.assertEqual(self.combined_names, full_name)

    # def test_add_new_user(self):
    #     self.assertCountEqual(add_new_user(self.combined_names, self.contact, self.email), self.all_users)

    def test_submit(self):
        resp =  add_new_user(self.combined_names, self.contact, self.email)
        self.assertEqual(resp, True)
