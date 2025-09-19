

def update_user_phone(username, phone):
    safe_username = escape_sql_string(username)
    safe_phone = escape_sql_string(phone)

    sql = f"UPDATE USER SET PHONE = '{safe_phone}' WHERE USERNAME = '{safe_username}';"
    return sql