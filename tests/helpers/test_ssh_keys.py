from unittest import TestCase

from gitSwitch.helpers.ssh_keys import create_key_pair
from mock import patch, MagicMock, call, mock_open

SOME_PRIVATE_KEY = 'some private key'
SOME_PUBLIC_KEY = 'some public key'


class TestSSHKeys(TestCase):
    @patch('gitSwitch.helpers.ssh_keys.generate')
    def test_generate_private_key_creates_file(self, mock_generate):
        m = mock_open()
        with patch('gitSwitch.helpers.ssh_keys.open', m):
            self.some_private_key(mock_generate)

            private_key, public_key = create_key_pair('some_path/', 'some_alias')

            self.assertEqual(private_key, SOME_PRIVATE_KEY)
            self.assertEqual(public_key, SOME_PUBLIC_KEY)
            self.assertIn(call('some_path/some_alias_rsa', 'w+'), m.mock_calls)
            self.assertIn(call('some_path/some_alias_rsa.pub', 'w+'), m.mock_calls)
            self.assertIn(call().write(SOME_PRIVATE_KEY), m.mock_calls)
            self.assertIn(call().write(SOME_PUBLIC_KEY), m.mock_calls)

    def some_private_key(self, mock_generate):
        mock_key = MagicMock()
        mock_key.exportKey.return_value = SOME_PRIVATE_KEY
        ex_key = MagicMock()
        ex_key.exportKey.return_value = SOME_PUBLIC_KEY
        mock_key.publickey.return_value = ex_key

        mock_generate.return_value = mock_key
