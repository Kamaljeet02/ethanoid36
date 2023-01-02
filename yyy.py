x=int(input("x: "))
y=int(input("Y: "))
print(x/y)
print(x//y)
print(x%y)

a=int(input("how many terms ?"))
n1,n2=0,1
count=0
if a,=0:
    print("please enter positive integer")
elif a==1:
    print("Fibonacci sequence upto",a,":")
    print(n1)
else:
    print("Fibonacci sequence")
    while count <a:
        print(n1)
        b=n1+n2
        n1=n2
        n2=b
        count+=1
