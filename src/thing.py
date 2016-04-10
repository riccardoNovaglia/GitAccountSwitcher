from SSHKeys import *
from Files import *
from GithubHelper import GithubHelper
from getpass import getpass

path = "./fakessh/"
ssh_config_file_path = path + "fake_config"
private_key_filename_template = "{}/{}_rsa"
public_key_filename_template = "{}/{}_rsa.pub"


def prompt_user():
    username_input = raw_input("Please input your username\n")
    email_input = raw_input("Please input your email\n")
    # TODO: validate
    alias_input = raw_input("Please input an alias for this git account\n")
    return username_input, email_input, alias_input


def append_email_to(pubkey):
    return pubkey.exportKey('OpenSSH') + ' {}'.format(email)


username, email, alias = prompt_user()

# generate ssh key
private_key, public_key = get_ssh_key_pair()
public_key = append_email_to(public_key)

write_to_file(private_key_filename_template.format(path, alias), private_key)
write_to_file(public_key_filename_template.format(path, alias), public_key)

append_to_file(ssh_config_file_path, get_ssh_config(alias))

github_password = getpass('Please provide your github password for username {}'.format(username))
github = GithubHelper(username, github_password)
github.upload_key(alias, public_key)

# Upload to github (needs username and pass) ?prompt for github pass


# set account for current dir (git config user.name and user.mail to provided)
