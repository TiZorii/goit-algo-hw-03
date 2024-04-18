import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    
    if phone_number.startswith('380'):
        return '+' + phone_number
    else:
        return '+38' + phone_number

phone_number = "    +38(050)123-32-34"
normalized_phone = normalize_phone(phone_number)
print("Нормалізований телефонний номер:", normalized_phone)