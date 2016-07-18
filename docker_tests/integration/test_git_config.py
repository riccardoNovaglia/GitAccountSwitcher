from unittest import TestCase

from assertpy import assert_that
from gitSwitch.helpers.git_config import GitConfig


class TestGitConfig(TestCase):
    username = 'user'
    email = 'email'
    expected_username = 'name = user'
    expected_mail = 'email = email'
    expected_remote = 'url = git@github.com:user/GitAccountSwitcher.git'
    expected_headers = ['[remote "origin"]', '[user]']

    def test_something(self):
        path = '/gitAccountSwitcher/.git/config'
        config = GitConfig(path)
        config.update_git_config(self.username, self.email)

        assert_that(self.file_text(path)).contains(self.expected_username)
        assert_that(self.file_text(path)).contains(self.expected_mail)
        assert_that(self.file_text(path)).contains(self.expected_remote)
        for header in self.expected_headers:
            assert_that(self.file_text(path)).contains(header)

    def file_text(self, filename):
        with open(filename, 'r') as my_file:
            data = my_file.read()
        return self.remove_newlines_and_tabs(data)

    def remove_newlines_and_tabs(self, text):
        return text.replace("\n", " ").replace("  ", "").strip()
