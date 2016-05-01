from github import Github, GithubException


class GithubHelper:
    def __init__(self, username, password):
        github_instance = Github(username, password=password)
        self._authenticated_user = github_instance.get_user()
        # assigning variable to cause an exception in case of incorrect credentials
        self.username = self._authenticated_user.login

    def upload_key(self, alias, key):
        try:
            return self._authenticated_user.create_key(alias, key)
        except GithubException as exception:
            if 'key is invalid' in exception.data['errors'][0]['message']:
                raise KeyFormatException('Key <{}> with alias <{}> is not in valid format'.format(key, alias))
            else:
                raise DuplicateKeyException('Duplicate key found for alias <{}>'.format(alias))


class DuplicateKeyException(Exception):
    pass


class KeyFormatException(Exception):
    pass
