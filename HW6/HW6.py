import datetime

def days_between_two_dates(date_1,date_2):
	difference = date2 - date1
	return difference.days

def months_between_two_dates(date_1,date_2):
	difference = date2 - date1
	months = difference.days/30.4
	return int(months)

def years_between_two_dates(date_1,date_2):
	difference = date2 - date1
	years = difference.days/365.25
	return int(years)

if __name__ == '__main__':
	date1 = datetime.date(2000, 1, 1)
	date2 = datetime.date(2016, 10, 3)
	print("Days between " + str(date1) + " & " + str(date2) + " : " + str(days_between_two_dates(date1,date2)))
	print("Months between " + str(date1) + " & " + str(date2) + " : " + str(months_between_two_dates(date1,date2)))
	print("Years between " + str(date1) + " & " + str(date2) + " : " + str(years_between_two_dates(date1,date2)))