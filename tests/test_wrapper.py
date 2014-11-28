import unittest

import fakename
from fakename import wrapper


class CourtesyTests(unittest.TestCase):
    def test_user_agent(self):
        """
        User-agent starts with py-fakename-
        """
        user_agent = False
        for header, value in wrapper.opener.addheaders:
            if header == 'User-Agent':
                user_agent = (value.startswith('py-fakename-'))
                break

        self.assertTrue(user_agent)


class IdentityTests(unittest.TestCase):
    IDENTITY_KEYS = {'name', 'dob', 'address', 'city', 'state', 'zip', 'phone', 'username', 'password', 'temp_email'}

    def test_return_format(self):
        identity = fakename.gen_identity()

        for key in self.IDENTITY_KEYS:
            self.assertTrue(identity[key])