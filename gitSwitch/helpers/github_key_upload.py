from github import Github, GithubException, BadCredentialsException
from gitSwitch.helpers.user_input import get_password


def upload_github_key_for_username(username, alias, key):
    github_instance = _log_into_github(username)

    _upload_key(github_instance, alias, key)


def _log_into_github(username):
    github_instance = Github(username, password=(get_password()))
    return github_instance.get_user()


def _upload_key(github_instance, alias, key):
    try:
        return github_instance.create_key(alias, key)
    except BadCredentialsException as exception:
        raise exception
    except GithubException as exception:
        if 'key is invalid' in exception.data['errors'][0]['message']:
            raise KeyFormatException('Key <{}> with alias <{}> is not in valid format'.format(key, alias))
        else:
            raise DuplicateKeyException('Duplicate key found for alias <{}>'.format(alias))


class DuplicateKeyException(Exception):
    pass


class KeyFormatException(Exception):
    pass
