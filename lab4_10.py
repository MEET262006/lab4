#fibonacci series
n=int(input("enter the number of terms:"))
a=0
b=1
if n<=0:
    print("invalid input")
elif n==1:
    print(a)
else:
    print(a,b,end=" ")
    for _ in range(2,n):
        c=a+b
        print(c,end=" ")
        a,b=b,c
