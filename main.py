from datetime import date
from application import salary as salary1
from application.db import people as people1

if __name__ == '__main__':
    date = date.today()
    print(date)
    print(people1.get_employees(), salary1.calculate_salary())