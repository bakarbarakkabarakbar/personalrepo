def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	initialyear = 2000
	initialmonth = 1
	outputdays = 0
	for a in range (initialyear, year+1):
		for b in range(initialmonth, month):
			outputdays += daysInMonth(a, b)
	return outputdays+day

print(dayOfYear(2000, 4, 20))