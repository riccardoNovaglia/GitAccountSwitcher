from Crypto.PublicKey.RSA import generate


def create_key_pair(files_destination_path, keys_alias):
    key = generate(2048)

    private_key = _create_private_key(files_destination_path, key, keys_alias)
    public_key = _create_public_key(files_destination_path, key, keys_alias)

    return private_key, public_key


def _create_public_key(files_destination_path, key, keys_alias):
    public_key = key.publickey().exportKey('OpenSSH')
    with open(files_destination_path + keys_alias + '_rsa.pub', 'w+') as file_stream:
        file_stream.write(public_key)
    return public_key


def _create_private_key(files_destination_path, key, keys_alias):
    private_key = key.exportKey('PEM')
    with open(files_destination_path + keys_alias + '_rsa', 'w+') as file_stream:
        file_stream.write(private_key)
    return private_key
