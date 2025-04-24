from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
import datetime
import requests as r

date = datetime.date.today()

google = r.get('https://www.google.com/search?q=')

if __name__ == '__main__':
    print(date, cs())
    print(date, ge())
    print(f'Код доступности гугла при помощи библиотеки requests: {google.status_code}')