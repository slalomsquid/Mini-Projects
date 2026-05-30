"""This is an implementation of Conway's doomsday algorithm used to find the day of the week of any given day"""
day = int(input("Day: ").strip())
month = int(input("Month: ").strip())
year = (input("Year: ")).strip()

day_code = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]
"""List of days starting from sunday (0), used to convert the sum number into a word"""

century_pattern = [2,0,5,3]
"""Century starting doomsday pattern, always Tuesdat, Sunday, Friday or """

doomsdays = [
    0, # Blank because lists start at 0
    3, # Jan # 4th on a leap year
    28, # Feb # 29th on leap
    14, # March
    4, # April
    9, # May
    6, # Jun
    11, # July
    8, # Aug
    5, # Sept
    10, # Oct
    7, # Nov
    12 # Dec
]
"""Doomsdays are always the same within a year, once it has been calculated, it can be used to find any given days"""

offset = 0
# Get century number
century = int(year[:2])
print(f"Century: {century}")
# year_century_code = int(century_doomsday.get(century, 0))
# Follow pattern from year 2000, (2,0,5,3)
year_century_code = century_pattern[(century-20)%4]
print(f"Year code: {year_century_code}")
# Get years into century (last 2 numbers)
years_in_century = int(year[2:])
print(f"Year: {years_in_century}")
if month < 3 and years_in_century % 4 == 0:
    print("Leap year")
    offset = 1
# Divide by 12
twelves = years_in_century // 12
print(f"Twelves in {years_in_century}: {twelves}")
# Get remainder
remainder = years_in_century % 12
print(f"Remainder: {remainder}")
# Get fours in remainder (accounts for leap years)
fours = remainder // 4
print(f"Fours in remainder: {fours}")
# Add together
sum = year_century_code + twelves + remainder + fours
print(f"Sum: {sum}")
# Get remainder after dividing by 7
doomsday = sum % 7
print(f"Doomsday: {doomsday}")
# Get doomsday of that month
month_doomsday = doomsdays[month]
print(f"Month doomsday: {month_doomsday}")
print(f"Day: {day}")
# Calculate days from referance doomstday, adding offset to account for leap yeay
days_from = day - (month_doomsday + offset)
print(f"Days from: {days_from}")
# Add year doomsday offset and find remainder (simplifys to range of 0-6)
day_of_week = (days_from + doomsday) % 7
print(day_code[day_of_week])