n=int(input("enter n"))
x=0
z=n
while n>0:
        r=n%10
        x=x*10+r
        n=n//10
if(x==z):
    print("palindrome")

else:
    print("na")
