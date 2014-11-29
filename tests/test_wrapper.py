import unittest

import fakename
from fakename import wrapper


class CourtesyTests(unittest.TestCase):
    def test_user_agent(self):
        """
        User-agent starts with py-fakename-
        """
        self.assertEqual(wrapper.session.headers['User-Agent'], 'py-fakename-' + fakename.__version__)


class IdentityTests(unittest.TestCase):
    IDENTITY_KEYS = {'name', 'dob', 'address', 'city', 'state', 'zip', 'phone',
                     'username', 'password', 'temp_email', 'permalink'}

    def test_return_format(self):
        """
        Asserts that the identity dict matches the declared format
        """
        identity = fakename.gen_identity()

        for key in self.IDENTITY_KEYS:
            self.assertTrue(identity[key])

    def test_parser_state_clears(self):
        """
        Makes sure that our PageParser class clears state between function calls
        """
        id1 = fakename.gen_identity()
        id2 = fakename.gen_identity()

        # the two identities should not be exactly equal
        all_equal = True
        for key in self.IDENTITY_KEYS:
            all_equal = all_equal and (id1[key] == id2[key])

        self.assertFalse(all_equal)