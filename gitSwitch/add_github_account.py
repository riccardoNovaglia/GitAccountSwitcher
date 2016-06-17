from helpers.ssh_keys import create_key_pair
from helpers.upload_github_key import upload_github_key
from os.path import expanduser


def add_github_account(email, username, password, alias):
    private_key, public_key = create_key_pair(expanduser('~/.ssh/'), alias)

    # TODO: write_to_file(ssh_config_file_path, get_ssh_config(user_input.get_account_alias()), 'a+')

    upload_github_key(username, password, alias, public_key)

    print "Public key for user {} uploaded successfully with alias {}".format(username, alias)

    # TODO: set account for current dir (git config user.name and user.mail to provided) also change remote
