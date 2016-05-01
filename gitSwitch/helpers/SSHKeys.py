from Crypto.PublicKey import RSA


def get_ssh_key_pair():
    key = RSA.generate(2048)
    private_key = key.exportKey('PEM')
    public_key = key.publickey()
    return private_key, public_key


def get_ssh_config(alias):
    return "\n\n" \
           "# {} github account\n" \
           "Host github-{}\n" \
           "   HostName github.com\n" \
           "   User git\n" \
           "   IdentityFile ~/.ssh/{}_rsa".format(alias, alias, alias)
