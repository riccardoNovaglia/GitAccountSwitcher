from unittest import TestCase

from gitSwitch.helpers.upload_github_key import DuplicateKeyException, KeyFormatException
from gitSwitch.helpers.upload_github_key import upload_github_key
from github import GithubException, BadCredentialsException
from mock import patch


class TestGithubHelper(TestCase):
    @patch('gitSwitch.helpers.upload_github_key.Github')
    def test_uploads_key(self, github_mock):
        # given
        github_mock.return_value = GithubMock()

        # when
        upload_github_key('some user', 'some pass', 'someAlias', 'someKey')

    @patch('gitSwitch.helpers.upload_github_key.Github')
    def test_throws_exception_if_bad_credentials(self, github_mock):
        # given
        github_mock.return_value = GithubMock(login_exception_class=BadCredentialsException)

        # when
        try:
            upload_github_key('someUser', 'some pass', 'someAlias', 'someKey')
            self.fail('Should have thrown bad credentials exception')
        except GithubException as exception:
            # then
            self.assertIsInstance(exception, BadCredentialsException)

    @patch('gitSwitch.helpers.upload_github_key.Github')
    def test_raises_duplicate_key_error(self, github_mock):
        # given
        key_alias = 'someDuplicateAlias'
        exception_data = {'errors': [{'message': 'key is already in use'}]}
        github_mock.return_value = GithubMock(key_upload_exception_class=GithubException, exception_data=exception_data)

        # when
        try:
            upload_github_key('some user', 'some pass', key_alias, 'someKey')
            self.fail('Should have raised duplicate key exception')
        except DuplicateKeyException as exception:
            self.assertEqual(exception.message, 'Duplicate key found for alias <{}>'.format(key_alias))

    @patch('gitSwitch.helpers.upload_github_key.Github')
    def test_raises_incorrect_key_format(self, github_mock):
        # given
        key_alias = 'someAlias'
        key_value = 'someKeyValue'
        exception_data = {'errors': [{'message': 'key is invalid yada yada yada'}]}
        github_mock.return_value = GithubMock(key_upload_exception_class=GithubException, exception_data=exception_data)

        # when
        try:
            upload_github_key('some user', 'some pass', key_alias, key_value)
            self.fail('Should have raised duplicate key exception')
        except KeyFormatException as exception:
            self.assertEqual(exception.message,
                             'Key <{}> with alias <{}> is not in valid format'.format(key_value, key_alias))


class GithubMock:
    def __init__(self, login_exception_class=None, key_upload_exception_class=None, exception_data=None):
        self.login_exception_class = login_exception_class
        self.key_upload_exception_class = key_upload_exception_class
        self.exception_data = exception_data

    def get_user(self):
        return self

    def create_key(self, alias, key):
        if self.login_exception_class:
            raise self.login_exception_class(None, self.exception_data)
        if self.key_upload_exception_class is not None:
            raise self.key_upload_exception_class(None, self.exception_data)
        else:
            return None
