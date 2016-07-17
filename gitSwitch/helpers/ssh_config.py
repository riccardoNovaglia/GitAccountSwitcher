def update_ssh_config(file_name, alias, username):
    with open(file_name, 'a+') as my_file:
        my_file.write(config_section_template.format(alias, username))


config_section_template = """

#{0} account
Host github.com-{1}
    HostName github.com
    User git
    IdentityFile ~/.ssh/{0}_rsa"""
