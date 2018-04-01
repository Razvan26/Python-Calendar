import time
import calendar

month = int(input("Enter mouth : "))

if month == 1:
    mshow = calendar.month(2018, 1)
elif month == 2:
    mshow = calendar.month(2018, 2)
elif month == 3:
    mshow = calendar.month(2018, 3)
elif month == 4:
    mshow = calendar.month(2018, 4)
elif month == 5:
    mshow = calendar.month(2018, 5)
elif month == 6:
    mshow = calendar.month(2018, 6)
elif month == 7:
    mshow = calendar.month(2018, 7)
elif month == 8:
    mshow = calendar.month(2018, 8)
elif month == 9:
    mshow = calendar.month(2018, 9)
elif month == 10:
    mshow = calendar.month(2018, 10)
elif month == 11:
    mshow = calendar.month(2018, 11)
elif month == 12:
    mshow = calendar.month(2018, 12)
else:
    print("1 to 12")
print(mshow)

