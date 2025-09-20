def escape_sql(value: str) -> str:
    """Ochrana proti SQL Injection"""
    return value.replace("'", "''")

def insert_post(nickname: str, text: str) -> str:
    nickname = escape_sql(nickname)
    text = escape_sql(text)
    return f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname}', '{text}');"

def update_phone(username: str, phone: str) -> str:
    username = escape_sql(username)
    phone = escape_sql(phone)
    return f"UPDATE USER SET PHONE='{phone}' WHERE USERNAME='{username}';"

def update_email(username: str, email: str) -> str:
    username = escape_sql(username)
    email = escape_sql(email)
    return f"UPDATE ACCOUNT SET EMAIL='{email}' WHERE USERNAME='{username}';"