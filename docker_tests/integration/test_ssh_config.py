from unittest import TestCase

from assertpy import assert_that
from gitSwitch.helpers.ssh_config import update_ssh_config
from os.path import exists


class TestSshConfig(TestCase):
    alias = "alias"
    username = "username"

    expected_config = """#alias account
    Host github.com-username
    HostName github.com
    User git
    IdentityFile ~/.ssh/alias_rsa"""

    def test_should_create_a_new_file_if_it_did_not_exist(self):
        non_existing_filename = "/tmp/some_file.txt"
        assert_that(exists(non_existing_filename)).is_false()

        update_ssh_config(non_existing_filename, self.alias, self.username)

        assert_that((exists(non_existing_filename))).is_true()
        assert_that(self.file_text(non_existing_filename)).contains(self.remove_newlines_and_tabs(self.expected_config))

    def test_should_append_to_the_file_without_changing_existing_content(self):
        some_existing_filename = "/etc/hostname"
        assert_that(exists(some_existing_filename)).is_true()

        original_file_content = self.file_text(some_existing_filename)
        assert_that(original_file_content).is_not_empty()

        update_ssh_config(some_existing_filename, self.alias, self.username)

        # content + ' ' to ensure at least one new line was placed before the new config
        assert_that(self.file_text(some_existing_filename)).contains(original_file_content + ' ')
        assert_that(self.file_text(some_existing_filename)).contains(
                self.remove_newlines_and_tabs(self.expected_config))

    def file_text(self, filename):
        with open(filename, 'r') as my_file:
            data = my_file.read()
        return self.remove_newlines_and_tabs(data)

    def remove_newlines_and_tabs(self, text):
        return text.replace("\n", " ").replace("  ", "").strip()
