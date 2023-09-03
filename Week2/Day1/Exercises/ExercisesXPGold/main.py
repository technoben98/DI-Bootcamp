#1
print("\nHello World"*4,"\nI love pyton"*4)

#2

month = int(input("Choose month \"from 1 to 12\"\n"))

if month >=3 and month < 6:
    print("Now it's Spring")
elif month >=6 and month < 9:
    print("Now it's Summer")
elif month >= 9 and month < 12:
    print("Now it's Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Now it's Winter")
else:
    print("Wrong month")