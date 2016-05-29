from getpass import getpass


def get_email():
    return UserInput.get_value_for('email', 'Please enter your Github email\n')


def get_username():
    return UserInput.get_value_for('name', 'Please enter your Github username\n')


def get_account_alias():
    return UserInput.get_value_for('alias', 'Please enter an alias for this account\n')


def get_password():
    return UserInput.get_sensitive_value_for('password', 'Please enter your Github password\n')


class UserInput:
    values = dict()

    def __init__(self):
        pass

    @classmethod
    def get_value_for(cls, key, prompt):
        if cls.value_exists_for(key) is None:
            cls.values[key] = raw_input(prompt)
        return cls.values[key]

    @classmethod
    def get_sensitive_value_for(cls, key, prompt):
        if cls.value_exists_for(key) is None:
            cls.values[key] = getpass(prompt)
        return cls.values[key]

    @classmethod
    def value_exists_for(cls, key):
        try:
            return cls.values[key]
        except KeyError:
            return None
