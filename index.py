from sql_utils import insert_post, update_phone, update_email
from password_utils import password_policy_check
from text_utils import censor_text, count_words

#SQL
print(insert_post("Eva", "Dobrý den všem!"))
print(update_phone("Eva", "123456789"))
print(update_email("Eva", "eva@example.com"))

# hesla
print(password_policy_check("Eva", "Stroasdangs1!"))
print(password_policy_check("Eva", "eva123456789"))

#cenzury
print(censor_text("Potkal jsem Járu Cimrmana a Ondřeje Mandíka."))

# počítání slov
print(count_words("I’ll go to 25 Londýnská, Praha 2013"))
# telefon
sql = update_phone("Eva", "123456789")
print(sql)
