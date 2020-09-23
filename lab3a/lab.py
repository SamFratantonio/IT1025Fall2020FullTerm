import datetime
now = datetime.datetime.now()
#this is a comment
def calcBday(bdate):
  return now.year - bdate.year - ((now.month, now.day) < (bdate.month, bdate.day)) 
  '''
  if true returns 1, if not returns 0, thereby subtracting 1
  if your birthday this year has not happened yet
  '''
print("Hello World!")
num1 = 5
num2 = 2
message = "new message"
quotient = num1 / num2
print(quotient)
remainder = num1 % num2
print(remainder)
age = int(input("Enter Your Age: "))
if age < 18:
  print("You Cannot Vote Yet\n")
else: 
  print("Please Vote!\n")
km = input("Enter how many kilometers you drove: ")
miles = float(km) * 0.62
print("You drove " + str(miles) + " miles\n")
print("What is your birthday?\nPlease write the date in this format (day/month/year)")
dateRaw = str(input(">"))
dateRaw = dateRaw.replace('\\', '/')
dateListA = dateRaw.split('/')
bDate = datetime.datetime(int(dateListA[2]), 
int(dateListA[0]), int(dateListA[1]))
if (bDate > now):
  print("You have not been born yet")
else:
  print("You Are " + str(calcBday(bDate)) + " Years Old")
