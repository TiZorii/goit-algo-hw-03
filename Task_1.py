def get_days_from_today(date):
    from datetime import datetime
    
    current_date = datetime.now().date()
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    days_difference = (current_date - given_date).days
    return days_difference


date = '2021-10-09'
days_difference = get_days_from_today(date)
print("Різниця в днях:", days_difference)
