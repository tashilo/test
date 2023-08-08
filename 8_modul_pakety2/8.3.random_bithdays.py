from datetime import datetime, timedelta
import random

def get_random_birthdays(n):
    """Отримати список випадкових днів нардження"""
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*80)
    youngest_date = current_date - timedelta(days=365*18)
    birthdays_list = []
    for i in range(n):
        fake_year = random.randrange(oldest_date.year, youngest_date.year)
        fake_month = random.randint(1, 12)
        fake_day = random.randint (1, 31)
        try:
            fake_birthday = datetime(year=fake_year, month=fake_month, day=fake_day) 
        except:
            continue    
        birthdays_list.append(fake_birthday.date())

    return birthdays_list   






if __name__ == '__main__':
    birthdays_list = get_random_birthdays(10)
    print(random.shuffle(birthdays_list))  
