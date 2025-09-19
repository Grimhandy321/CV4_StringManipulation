import re


def checkPassword(username, password):

    if len(password) < 10:
        return False

    if not re.search(r"\d", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[^a-zA-Z0-9]", password):
        return False
    if username.lower() in password.lower():
        return False
    username = username.lower()
    password_lower = password.lower()

    for i in range(len(username) - 3):
        for j in range(i + 4, len(username) + 1):
            substring = username[i:j]
            if substring in password_lower:
                return False
    return True