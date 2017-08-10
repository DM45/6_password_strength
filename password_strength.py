import string


def get_password_strength(password):
    pass_stren_lvl = 1
    if len(set(string.digits).intersection(password)):
        pass_stren_lvl += 3
    if (len(set(string.ascii_lowercase).intersection(password)) and
            len(set(string.ascii_uppercase).intersection(password))):
        pass_stren_lvl += 3
    if len(set("~`!@#$%^&*()_-+={}[]:>;',</?*-+").intersection(password)):
        pass_stren_lvl += 3
    return pass_stren_lvl


if __name__ == '__main__':
    _password = input('Enter password: ')
    print('Password strength: ')
    print(get_password_strength(_password))
