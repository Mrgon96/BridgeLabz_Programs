import sys

#function to return value of day in integer
def day(d,m,y):
    y0= y - (( 14 - m)/12)
    x = y0 + y0/4 - y0/100 + y0/400
    m0 = m + 12 *((14 - m)/12) - 2
    d0 = (d + x + ((31 * m0)/12))%7
    return d0


#checking for leap year
def leapYear(year):
    if year%4==0 and year%100!=0 or year%400 == 0:
        return True

    return False


# inputs from command line
month = int(sys.argv[1])
year = int(sys.argv[2])


#lists for months and dates
months = [0,'January','February','March','April','May','June','July','August','September','October','November','December']
days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


#print month and year
print('%s  '%months[month]),
print('%d '%year)
week=['S','M','T','W','Th','F','S']

# print week days
for w in week:
    print(w),
    print('\t'),

# checking for leap year
if month==2 and leapYear(year):
    days[month] = 29


print

#initializing day of month as first
d = day(1,month,year)



for i in range(d):
    print('\t'),

# printing dates of month
for j in range(1,days[month]+1):
    print(j),
    print('\t'),
    if (j+ d) % 7 == 0 or j == days[month]:
        print

