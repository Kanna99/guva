a=int(input("enter the year"))
if(a%4==0 or a%100!=0 or a%400==0):
   print("given year is leap year")
else:
   print("given is not leap year")
