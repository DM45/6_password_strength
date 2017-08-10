import string


def get_password_strength(password):
    k = 1
    if len(set(string.digits).intersection(password)) > 0:
        k += 3
    if len(set(string.ascii_letters).intersection(password)) > 0:
        k += 3
    if len(set("~`!@#$%^&*()_-+={}[]:>;',</?*-+").intersection(password)) > 0:
        k += 3
    return k


if __name__ == '__main__':
    _password = input('Enter password: ')
    print('Security level of your password:')
    print(get_password_strength(_password))
