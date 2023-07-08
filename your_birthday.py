import datetime

birthday = input('Enter your birthday (YYYY-MM-DD): ')
today = datetime.date.today()

day_diff = (today - datetime.date.fromisoformat(birthday)).days

print('You are turned: ')
print('Days: ', day_diff)
print('Hours: ', day_diff * 24)
print('Minutes: ', day_diff * 24 * 60)
print('Seconds: ', day_diff * 24 * 60 * 60)
