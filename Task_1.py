def get_days_from_today(date):
    from datetime import datetime
    
    try:
        current_date = datetime.now().date()
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        days_difference = (current_date - given_date).days
        return days_difference
    except ValueError:
        return "Невірний формат дати. Будь ласка, використовуйте формат: YYYY-MM-DD"


date = input("Введіть дату у форматі YYYY-MM-DD: ")
days_difference = get_days_from_today(date)
print("Різниця в днях:", days_difference)
