from datetime import datetime

def get_days():
    "Скріпт розрахунку кількості днів до заданої дати"
    user_input = input("Введіть дату до якої потрібно розрахувати кількість днів (формат dd:mm): ")
    user_date = datetime.strptime(user_input, '%d.%m')
    current_date = datetime.now()
    user_date = user_date.replace(year=current_date.year)
    delta_days = user_date - current_date
    target_date = datetime.strftime(user_date, '%d-%B-%Y')
    if delta_days.days > 0:
        print(f'осталось {delta_days.days} дней до {target_date}')
    else:
        user_date = user_date.replace(year=current_date.year + 1) 
        delta_days = user_date - current_date   
        print(f'осталось {delta_days.days} дней до {target_date}')


if __name__ == '__main__':
    get_days()    

