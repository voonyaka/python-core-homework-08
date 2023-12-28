from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Створюємо словник для збереження списку імен за дніми тижня
    users_list = defaultdict(list)
    
    # Отримуємо поточну дату
    today_date = date.today()
    
    # Отримуємо поточний рік
    current_year = today_date.year
    
    # Визначаємо інтервал тижня
    week_interval = timedelta(days=7)
    
    # Перевіряємо, чи є користувачі
    if not users:
        return users_list

    # Ітеруємося по користувачам
    for dictionary in users:
        # Отримуємо день народження та замінюємо рік на поточний (або на наступний рік, якщо січень)
        user_birthday = dictionary["birthday"].replace(year=current_year + 1 if dictionary["birthday"].month == 1 else current_year)
        
        # Перевіряємо, чи день народження в майбутньому або минув
        if user_birthday - today_date > week_interval or user_birthday < today_date:
            continue
        
        # Визначаємо день тижня та додаємо ім'я до відповідного списку
        birthday_weekday = user_birthday.weekday()
        users_list[user_birthday.strftime('%A') if birthday_weekday not in (5, 6) else "Monday"].append(dictionary["name"])

    return users_list

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    # Виводимо результат
    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

