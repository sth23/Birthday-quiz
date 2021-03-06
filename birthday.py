"""
birthday.py
Author: Sean Healey
Credit: Tutorials
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the Stone Age.
"""

from datetime import datetime
from calendar import month_name
today_month_num = datetime.today().month
today_date = datetime.today().day

today_month_name = month_name[today_month_num]

# Take user input
name = input("Hello, what is your name? ")
birth_month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
birth_year = int(input("And what year were you born in, {0}? ".format(name)))
birth_day = int(input("And the day? ".format(name)))

if today_month_name.lower() == birth_month.lower(): # Check for birthday
    print("Happy birthday!")
elif birth_month.lower() == "october" and birth_day == 31: # Check for Halloween
    print("You were born on Halloween!")
else:
    # Determine birth season
    if birth_month.lower() == "december" or birth_month.lower() == "january" or birth_month.lower() == "february":
        season = "winter"
    elif birth_month.lower() == "march" or birth_month.lower() == "april" or birth_month.lower() == "may":
        season = "spring"
    elif birth_month.lower() == "june" or birth_month.lower() == "july" or birth_month.lower() == "august":
        season = "summer"
    else:
        season = "fall"
    # Determin era
    if birth_year >= 2000:
        era = "two thousands"
    elif birth_year >= 1990:
        era = "nineties"
    elif birth_year >= 1980:
        era = "eighties"
    else:
        era = "Stone Age"
    print("{0}, you are a ".format(name) + season + " baby of the " + era + ".")
        
        
        
        
        
