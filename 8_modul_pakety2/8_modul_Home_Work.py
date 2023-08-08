from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today()
    end_of_week = today + timedelta(days=7)
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthday_week = {day: [] for day in weekdays}
    
    for user in users:
        user_birthday_this_year = user['birthday'].replace(year=today.year)
        
        if user_birthday_this_year < today:
            user_birthday_this_year = user_birthday_this_year.replace(year=today.year + 1)
        
        if today <= user_birthday_this_year < end_of_week:
            birthday_day = weekdays[user_birthday_this_year.weekday()]
            
            # Если день рождения в выходные, добавьте в понедельник
            if birthday_day in ['Saturday', 'Sunday']:
                birthday_day = 'Monday'
                
            birthday_week[birthday_day].append(user['name'])
    
    for day, names in birthday_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Тестовые данные
users = [
    {"name": "Bill", "birthday": datetime(1990, 8, 15)}, 
    {"name": "Jill", "birthday": datetime(1992, 8, 15)},
    {"name": "Kim", "birthday": datetime(1994, 8, 12)},
    {"name": "Jan", "birthday": datetime(1996, 8, 13)},
    {"name": "Bob", "birthday": datetime(1998, 8, 10)},
]

# Для теста:
get_birthdays_per_week(users)
