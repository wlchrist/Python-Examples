from datetime import datetime, timedelta

today = datetime.now()
# the now function returns a datetime object
print('Today is: ' + str(today))

#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# Storing an input
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# strptime is just a function that is able to convert a date input

print('Birthday: ' + str(birthday_date))

print()
