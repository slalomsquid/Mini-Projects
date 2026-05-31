* Doomsday.py:
  * This program is an implementation of Conway's Doomsday algorithm that can find the day of the week of any given date.
  * I am trying to learn to do this in my head, so i figured writing it out like this would help.
  * I have added lots of comments and detailed variable names so it can be followed along with.
  * Here are the steps the program follows:

    1. Get century code by getting the remainder of the century (first 2 digits) / 4, the code its the number at that index in the list [2,0,5,3]
    2. Check if the year (last 2 digits) is evenly divisible by 4, if so its a leap year, only an issue if month is jan or feb
    3. Get the ammount of times 12 goes into the year
    4. Get the remainder of that
    5. Get the ammount of times 4 fours into that remainder
    6. Add the century code, twelves, remainder and fours
    7. Get the remainder of the sum / 7, that is the doomsday week day (0 is sunday, 6 is saturday) of the year
    8. Get the doomsday of the target month
    9. Find the distance from the day to the doomsday, (add one to the doomsday if jan or feb and a leap year)
    10. Divide the distance by 7, the remainder is the day of the week
  * Example:

    22/11/1948

    1. 19%4 = 3, century code = 3
    2. 48/4 = 0, leap year
    3. 12/48 = 4
    4. 0
    5. 0
    6. 3 + 4 + 0 + 0 = 7
    7. 7%7 = 0
    8. 7
    9. 22-7 = 15
    10. 15%7 = 1
