import datetime

birthday = input("Enter your birthday (DD/MM/YYYY): ")
bday_day = int(birthday[0:2])
bday_month = int(birthday[3:5])
bday_year = int(birthday[6:10])

now = datetime.datetime.now()
current_day = int(now.day)
current_month = int(now.month)
current_year = int(now.year)

current_age = current_year - bday_year

if current_month<bday_month:
    current_age -= 1
elif current_month == bday_month:
    if current_day<bday_day:
        current_age -= 1

print(f"You are {current_age} years old!")

candles = None
if current_age < 10:
    candles = current_age
else:
    candles = str(current_age)[1]
    candles = int(candles)

candle_line = 'i'*candles
straight_line = '_'*(round((11-candles)/2))

print('    '+straight_line+candle_line+straight_line)
print('   |:H:a:p:p:y:|')
print(' __|___________|__')
print('|^^^^^^^^^^^^^^^^^|')
print('|:B:i:r:t:h:d:a:y:|')
print('|                 |')
print('~~~~~~~~~~~~~~~~~~~')