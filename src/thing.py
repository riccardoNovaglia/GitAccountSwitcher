from Crypto.PublicKey import RSA
from basicauth import encode

path = "./fakessh/"
sshfile = path + "fake_config"

# username = raw_input("Please input your username\n")
email = raw_input("Please input your email\n")
# TODO: validate
alias = raw_input("Please input an alias for this git account\n")

# generate ssh key
key = RSA.generate(2048).publickey()

with open("{}/{}".format(path, alias), 'w') as file_stream:
    private_key = key.exportKey('PEM')
    file_stream.write(private_key)

pubkey = key.publickey()

with open("{}/{}.pub".format(path, alias), 'w') as file_stream:
    public_key = pubkey.exportKey('OpenSSH') + ' {}'.format(email)
    file_stream.write(public_key)


# add to ssh_config using alias
with open(sshfile, "w") as file_stream:
    file_stream.write(
        "Host github-{}\n"
        "   HostName github.com\n"
        "   User git\n"
        "   IdentityFile {}".format(alias, alias)
    )

# Upload to github (needs username and pass) ?prompt for github pass
github

def post():
    pass
# set account for current dir (git config user.name and user.mail to provided)
