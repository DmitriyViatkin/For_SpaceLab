"""Генератор розкладу

Створіть функцію, яка генерує розклад робочих днів працівника.

➡️ Умови: 

    Функція приймає кількість днів, на які потрібно скласти розклад, кількість днів роботи, кількість днів відпочинку та дату початку розкладу.
    Функція повертає розклад робочих днів співробітника, який генерується починаючи з start_date на days днів уперед, враховуючи що співробітник чергує робочі дні (work_days) та дні відпочинку (rest_days).
    Функція має повернути дані у форматі List[datetime.datetime]

Тести:

days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30) ->
[
datetime.datetime(2020, 1, 30, 0, 0),
datetime.datetime(2020, 1, 31, 0, 0),
  datetime.datetime(2020, 2, 2, 0, 0),
datetime.datetime(2020, 2, 3, 0, 0)
]"""
import datetime


days =5
work_days= 2
rest_days= 1
start_date= datetime.date(2020, 1, 30)
work=[]
rest=[]

def work_day(day,work_days,rest_days,start_date):
    
    counts=0
    for count in range (days):
        
        if counts<work_days:
            work.append(start_date)
            start_date =start_date + datetime.timedelta(days=1)
            counts+=1
            
        elif counts>=work_days:
            for rez in range (rest_days):
              rest.append(start_date)
              start_date =start_date + datetime.timedelta(days=1 )
              
            counts=0

    return work, rest


work_day(days,work_days,rest_days,start_date)


print('Work days',work)
print('Rest days',rest)