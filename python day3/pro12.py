i1=input("Enter the first value :")
i2=input("Enter the second value :")
i3=input("Enter the third value :")

if i1>=i2:
    if i1>=i3:
        print("{} is the greatest value".format(i1))
    else:
        print("{} is the greatest value".format(i3))

else:
    if i2>=i3:
        print("{} is the greatest value".format(i2))
    else:
        print("{} is the greatest value".format(i3))