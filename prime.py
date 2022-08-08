a=int(input("enter n"))
x=0
for i in range (1,a):
    if(a%i == 0):
        x=x+1


if(x==2):
    print("it is prime")
else:
    print("not a prime")