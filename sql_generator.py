def genrateInsert(nickname,text):
       return F"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ({nickname},{text});"
def sanatizeInput(value):
    value = value.replace("'", "''")
    value = value.replace(";", "")
    value = value.replace("--", "")
    value = value.replace("\\", "")
    value = value.replace('"', "")
    return value