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

import ggame

from datetime import datetime
from calendar import month_name
today_month_num = datetime.today().month
today_date = datetime.today().day

today_month_name = month_name[today_month_num]

name = input("Hello, what is your name? ")
birth_month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
birth_year = int(input("And what year were you born in, {0}? ".format(name)))
birth_day = int(input("And the day? ".format(name)))

if today_month_name.lower() == birth_month.lower():
    print("Happy birthday!")
elif birth_month.lower() == "october" and birth_day == 31:
    print("You were born on Halloween!")
else:
    print("Something else")
