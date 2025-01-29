n=int(input("enter the number"))
if n<0:
      print("invalid input")
elif n==0:
      print("the factorial of 0 is 1")
else:
      fact=1
      for i in range(1,n+1):
          fact=fact*i
      print(f"the factoril of {n} is {fact}")
