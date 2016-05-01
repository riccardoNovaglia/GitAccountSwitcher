import unittest

from SSHKeys import get_ssh_key_pair
from github import AuthenticatedUser, BadCredentialsException, Github, GithubException

username = ''
account_password = ''


@unittest.skipIf(username == account_password == '', 'Skipping tests due to missing credentials')
class LearningGithub(unittest.TestCase):

    def test_creates_instance(self):
        github_object = Github('someUsername', 'somePassword')

        self.assertIsInstance(github_object, Github)

    def test_returns_user_info_if_logged_in(self):
        github_user = Github(username, account_password).get_user()

        self.assertIsInstance(github_user, AuthenticatedUser.AuthenticatedUser)
        self.assertTrue(hasattr(github_user, 'create_key'))
        self.assertEqual(github_user.html_url, 'https://github.com/{}'.format(username))
        self.assertEqual(github_user.login, username)

    def test_get_user_does_not_throw_exception_if_bad_credentials(self):
        Github('wrongUser', 'wrongPass').get_user()

    def test_get_user_info_throws_exception_if_bad_credentials(self):
        github_user = Github('wrongUser', 'wrongPass').get_user()
        try:
            github_user.login
        except Exception as exception:
            self.assertIsInstance(exception, BadCredentialsException)

    def test_throws_an_exception_if_the_key_is_not_a_real_key(self):
        github_user = Github(username, account_password).get_user()
        try:
            github_user.create_key('someKeyAlias', 'keyValue')
        except Exception as exception:
            self.assertIsInstance(exception, GithubException)
            self.assertIn('key is invalid', exception.data['errors'][0]['message'])

    def test_throws_exception_when_key_is_duplicate(self):
        _, public_key = get_ssh_key_pair()
        github_user = Github(username, account_password).get_user()
        public_key = public_key.exportKey('OpenSSH')
        create_key_return = github_user.create_key('willBeDuplicatedAlias', public_key)
        try:
            github_user.create_key('willBeDuplicatedAlias', public_key)
        except Exception as exception:
            self.assertIsInstance(exception, GithubException)
            self.assertEqual(exception.data['errors'][0]['message'], 'key is already in use')
        github_user.get_key(create_key_return.id).delete()

    def test_returns_something_when_key_is_created(self):
        _, public_key = get_ssh_key_pair()
        github_user = Github(username, account_password).get_user()
        public_key = public_key.exportKey('OpenSSH')
        create_key_return = github_user.create_key('someTestKeyAlias', public_key)
        self.assertTrue(create_key_return.verified)
        key_id = create_key_return.id
        delete_key_return = github_user.get_key(key_id).delete()
        self.assertTrue(delete_key_return is None)
