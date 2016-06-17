from unittest import TestCase

from gitSwitch.add_github_account import add_github_account
from github import Github
from os.path import expanduser, exists


class TestAddGithubAccount(TestCase):
    def test_adding_a_new_key_creates_files_uploads_and_changes_config(self):
        username, password, email, alias = self.some_credentials()

        add_github_account(email, username, password, alias)

        private_key_content = self.private_keys_files_are_created_with_name(alias)
        self.public_key_is_uploaded_to_github(username, password, alias, private_key_content)
        self.git_config_for_the_repo_are_changed()

    def some_credentials(self):
        return "testRiccardo", "testgithub1234", "someEmail", "someAlias"

    def private_keys_files_are_created_with_name(self, alias):
        ssh_dir = expanduser('~/.ssh/')
        private_key_name = ssh_dir + alias + "_rsa"
        public_key_name = ssh_dir + alias + "_rsa" + ".pub"
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

    def git_config_for_the_repo_are_changed(self):
        pass

    def read_file(self, filename):
        with open(filename, 'r') as my_file:
            data = my_file.read().replace('\n', '')
        return data
