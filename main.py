import re

def get_days_from_today(date):
    from datetime import datetime
    
    current_date = datetime.now().date()
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    days_difference = (current_date - given_date).days
    return days_difference

def get_numbers_ticket(min_val, max_val, quantity):
    import random
    
    if not (1 <= min_val <= max_val <= 1000):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_val, max_val))
        
    return sorted(list(numbers))

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    
    if phone_number.startswith('380'):
        return '+' + phone_number
    else:
        return '+38' + phone_number


# Завдання 1
date = '2021-10-09'
days_difference = get_days_from_today(date)
print("Різниця в днях:", days_difference)

# Завдання 2
min_val = 1
max_val = 49
quantity = 6
lottery_numbers = get_numbers_ticket(min_val, max_val, quantity)
print("Ваші лотерейні числа:", lottery_numbers)

# Завдання 3
phone_number = "    +38(050)123-32-34"
normalized_phone = normalize_phone(phone_number)
print("Нормалізований телефонний номер:", normalized_phone)
