import re


import re

def password_policy_check(username: str, password: str) -> bool:
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
    for i in range(len(username) - 3):
        sub = username[i:i+4]
        if sub.lower() in password.lower():
            return False
    return True
