from sql_utils import escape_sql


def update_phone(username: str, phone: str) -> str:
    username = escape_sql(username)
    phone = escape_sql(phone)
    return f"UPDATE USER SET PHONE='{phone}' WHERE USERNAME='{username}';"
