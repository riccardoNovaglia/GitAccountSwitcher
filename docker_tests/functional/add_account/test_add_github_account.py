from unittest import TestCase

from assertpy import assert_that
from gitSwitch.add_github_account import add_github_account
from github import Github
from os.path import exists


class TestAddGithubAccount(TestCase):
    ssh_dir = '/root/.ssh/'

    def test_adding_a_new_key_creates_files_uploads_and_changes_config(self):
        username, password, email, alias = self.some_credentials()

        add_github_account(email, username, password, alias)

        private_key_content = self.private_keys_files_are_created_with_name(alias)
        self.ssh_config_are_updated(alias, username)
        self.public_key_is_uploaded_to_github(username, password, alias, private_key_content)
        self.git_config_for_the_repo_are_changed()

    def some_credentials(self):
        return "testRiccardo", "testgithub1234", "someEmail", "someAlias"

    def private_keys_files_are_created_with_name(self, alias):
        private_key_name = self.ssh_dir + alias + "_rsa"
        public_key_name = self.ssh_dir + alias + "_rsa" + ".pub"
        if not exists(private_key_name):
            self.fail("Private key not found under {}".format(private_key_name))
        if not exists(public_key_name):
            self.fail("Public key not found under {}".format(public_key_name))
        return self.read_file(public_key_name)

    def public_key_is_uploaded_to_github(self, username, password, alias, key_content):
        github_instance = Github(username, password=password)
        keys = github_instance.get_user().get_keys()
        for key in keys:
            if key.title == alias and key.key == key_content:
                key.delete()
                return

        self.fail("Could not find key for '{}' with content '{}'".format(alias, key_content))

    def ssh_config_are_updated(self, alias, username):
        config_file_name = self.ssh_dir + 'config'
        if not exists(config_file_name):
            self.fail('ssh config file not found at {}'.format(config_file_name))
        file_content = self.read_file(config_file_name)
        assert_that(file_content).contains(ssh_config_expected_value.format(alias, username))

    def git_config_for_the_repo_are_changed(self):
        self.fail("git config changes not implemented yet")

    def read_file(self, filename):
        with open(filename, 'r') as my_file:
            data = my_file.read()
        return data


ssh_config_expected_value = """
#{0} account
Host github.com-{1}
    HostName github.com
    User git
    IdentityFile ~/.ssh/{0}_rsa"""
