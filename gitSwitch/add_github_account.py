from helpers.ssh_config import update_ssh_config
from helpers.ssh_keys import create_key_pair
from helpers.upload_github_key import upload_github_key
from os.path import expanduser


def add_github_account(email, username, password, alias):
    private_key, public_key = create_key_pair(expanduser('~/.ssh/'), alias)

    update_ssh_config(expanduser('~/.ssh/config'), alias, username)

    upload_github_key(username, password, alias, public_key)

    print "Public key for user {} uploaded successfully with alias {}".format(username, alias)

    # TODO: set account for current dir (git config user.name and user.mail to provided) also change remote
