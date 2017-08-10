import string


def get_password_strength(password):
    k = 1
    if len(set(string.digits).intersection(password)) > 0:
        k += 3
    if ((len(set(string.ascii_lowercase).intersection(password)) > 0) and
            (len(set(string.ascii_uppercase).intersection(password)) > 0)):
        k += 3
    if len(set("~`!@#$%^&*()_-+={}[]:>;',</?*-+").intersection(password)) > 0:
        k += 3
    return k


if __name__ == '__main__':
    _password = input('Enter password: ')
    print('Password strength: ')
    print(get_password_strength(_password))
