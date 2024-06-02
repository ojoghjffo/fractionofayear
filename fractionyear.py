import math
import calendar

def yeardivide():
    try:
        numerator = float(input("Numerator: "))
        
        denominator = float(input("Denominator: "))
        leapyear = input("Add February 29? y/n ")
        isLeapYear = leapyear in ["y", "yes"]
        quotient = denominator / (365 + isLeapYear)
        day = math.ceil(numerator / quotient)
        hour = (numerator / quotient) - (math.floor(numerator / quotient))
        minute = (hour * 24 - math.floor(hour * 24))
        second = (minute * 60 - math.floor(minute * 60))
        zeromin = "0" if math.floor(minute * 60) < 10 else ""
        zerosec = "0" if math.floor(second * 60) < 10 else ""
        if numerator <= 0:
            print("Numerator must not be equal or less than zero")
            return
        
        if hour == 0:
            hour = 24
        
        if numerator > denominator:
            print("Numerator must not be greater than the Denominator")
            return
        cale = [31, 28 + isLeapYear, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = 1
        for days in cale:
            if day <= days:
                print(f"{calendar.month_name[month]} {day} at {math.floor(hour * 24) if hour != 24 else hour}:{zeromin}{math.floor(minute * 60)}:{zerosec}{math.floor(second * 60)}")
                return
            day -= days
            month += 1
        
    except ValueError:
        print("Invalid Value")
    except ZeroDivisionError:
        print("Denominator cannot be zero")

while True:
    yeardivide()
    print("")
