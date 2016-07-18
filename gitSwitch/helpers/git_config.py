import ConfigParser

from StringIO import StringIO


# TODO: what happens when the repo is not configured already?
class GitConfig:
    def __init__(self, config_filepath):
        self.config_filepath = config_filepath
        self.config = ConfigParser.ConfigParser()

        self.config.readfp(self._file_object(config_filepath))

    def update_git_config(self, username, email):
        self._set_user_properties(email, username)
        self._set_remote_properties(username)
        with open(self.config_filepath, 'wb') as configfile:
            self.config.write(configfile)

    def _set_user_properties(self, email, username):
        try:
            self.config.set('user', 'name', username)
            self.config.set('user', 'email', email)
        except ConfigParser.NoSectionError:
            self.config.add_section('user')
            self._set_user_properties(email, username)

    def _set_remote_properties(self, username):
        try:
            self.config.set('remote "origin"', 'url', 'git@github.com:{}/GitAccountSwitcher.git'.format(username))
        except ConfigParser.NoSectionError:
            self.config.add_section('remote "origin"')
            self._set_remote_properties(username)

    def _file_object(self, filename):
        return StringIO('\n'.join(line.strip() for line in open(filename)))
