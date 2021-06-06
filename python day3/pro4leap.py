user_in=int(input("Enter the Year :"))

if user_in%4==0:
    if user_in%100==0:
        if user_in%400==0:
            print("{} is a Leap Year".format(user_in))
        else:
            print("{} is not a Leap Year".format(user_in))
    else:
        print("{} is a Leap Year".format(user_in))
else:
    print("{} is not a Leap Year".format(user_in))