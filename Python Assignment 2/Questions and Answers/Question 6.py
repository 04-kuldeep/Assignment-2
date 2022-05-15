a=int(input("Enter a number"))
b=int(input("Enter a number"))
flips=0     #counter for flips required
while(a>0 and b>0):
    t1=a&1
    t2=b&1
    if(t1!=t2):
        flips+=1

        a>>=1
        b>>=1

        print("Total flips required is",flips)