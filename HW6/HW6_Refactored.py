import datetime

def dates_difference(date_1, date_2, units = None): # if nothing is provided as third argument than days between dates will be returned
    difference = date_2 - date_1
    if units == 'd' or units == 'D' or units is None:
        return difference.days
    elif units == 'm' or units == 'M':
        return int(difference.days / 30.4)
    elif units == 'y' or units == 'Y':
        return int(difference.days / 365.25)
    else:
        print("INVALID 3rd ARGUMENT: Provide D for days, Provide M for months and Provide Y for years")

if __name__ == '__main__':
    date1 = datetime.date(2000, 1, 1)
    date2 = datetime.date(2016, 10, 3)
    print("Days between " + str(date1) + " & " + str(date2) + " : " + str(dates_difference(date1,date2,'D')))
    print("Months between " + str(date1) + " & " + str(date2) + " : " + str(dates_difference(date1,date2,'M')))
    print("Years between " + str(date1) + " & " + str(date2) + " : " + str(dates_difference(date1,date2, 'Y')))