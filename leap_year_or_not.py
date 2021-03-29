year=int(input("Enter the year"))
if(year%4)==0 and (year%100)!=0:
    print("Year is a not leap year")
elif(year%400)==0:
    print("Year is a leap year")
else:
    print("not leap year")