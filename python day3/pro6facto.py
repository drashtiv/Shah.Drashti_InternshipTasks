value=int(input("Enter the value :"))
factorial=1
if value<0:
    print("No Factorial for Negative Numbers")
elif value==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,value+1):
        factorial=factorial*i
        print("The factorial of", value, "is", factorial)