from github import Github


class GithubHelper:
    def __init__(self, username, password):
        self._authenticated_user = Github(username, password=password).get_user()

    def upload_key(self, alias, key):
        return self._authenticated_user.create_key(alias, key)
