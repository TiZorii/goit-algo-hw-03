def get_numbers_ticket(min_val, max_val, quantity):
    import random
    
    if not (1 <= min_val <= max_val <= 1000):
        return []
    
    max_possible_numbers = max_val - min_val + 1
    if quantity > max_possible_numbers:
        return "Кількість чисел перевищує максимально можливу кількість."
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_val, max_val))
        
    return sorted(list(numbers))

min_val = 1
max_val = 49
quantity = 6
lottery_numbers = get_numbers_ticket(min_val, max_val, quantity)
print("Ваші лотерейні числа:", lottery_numbers)
