from unittest import TestCase

from gitSwitch.helpers.user_input import get_email, UserInput, get_username, get_password, get_account_alias
from mock import patch

EMAIL_PROMPT = 'Please input your Github email'
USERNAME_PROMPT = 'Please input your Github username'
ACCOUNT_ALIAS_PROMPT = 'Please input an alias for this account'
PASSWORD_PROMPT = 'Please input your Github password'
SOME_VALUE = 'something'


class TestUserInput(TestCase):
    def setUp(self):
        UserInput.values = dict()

    @patch('gitSwitch.helpers.user_input.raw_input')
    def test_request_user_email_calls_raw_input(self, mock_raw_input):
        mock_raw_input.return_value = SOME_VALUE

        returned = get_email()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_raw_input.called_once_with(EMAIL_PROMPT))

    @patch('gitSwitch.helpers.user_input.raw_input')
    def test_request_user_email_calls_raw_input_caches_result(self, mock_raw_input):
        mock_raw_input.return_value = SOME_VALUE
        get_email()

        returned = get_email()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_raw_input.called_once_with(EMAIL_PROMPT))
        self.assertEqual(mock_raw_input.call_count, 1)

    @patch('gitSwitch.helpers.user_input.raw_input')
    def test_request_user_username_calls_raw_input(self, mock_raw_input):
        mock_raw_input.return_value = SOME_VALUE

        returned = get_username()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_raw_input.called_once_with(USERNAME_PROMPT))

    @patch('gitSwitch.helpers.user_input.raw_input')
    def test_request_user_username_calls_raw_input_caches_result(self, mock_raw_input):
        mock_raw_input.return_value = SOME_VALUE
        get_username()

        returned = get_username()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_raw_input.called_once_with(USERNAME_PROMPT))
        self.assertEqual(mock_raw_input.call_count, 1)

    @patch('gitSwitch.helpers.user_input.raw_input')
    def test_request_account_alias_calls_raw_input(self, mock_raw_input):
        mock_raw_input.return_value = SOME_VALUE

        returned = get_account_alias()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_raw_input.called_once_with(ACCOUNT_ALIAS_PROMPT))

    @patch('gitSwitch.helpers.user_input.raw_input')
    def test_request_account_alias_calls_raw_input_caches_result(self, mock_raw_input):
        mock_raw_input.return_value = SOME_VALUE
        get_account_alias()

        returned = get_account_alias()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_raw_input.called_once_with(ACCOUNT_ALIAS_PROMPT))
        self.assertEqual(mock_raw_input.call_count, 1)

    @patch('gitSwitch.helpers.user_input.getpass')
    def test_request_user_password_calls_raw_input(self, mock_getpass):
        mock_getpass.return_value = SOME_VALUE

        returned = get_password()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_getpass.called_once_with(USERNAME_PROMPT))

    @patch('gitSwitch.helpers.user_input.getpass')
    def test_request_user_password_calls_raw_input_caches_result(self, mock_getpass):
        mock_getpass.return_value = SOME_VALUE
        get_password()

        returned = get_password()

        self.assertEqual(returned, SOME_VALUE)
        self.assertTrue(mock_getpass.called_once_with(USERNAME_PROMPT))
        self.assertEqual(mock_getpass.call_count, 1)
