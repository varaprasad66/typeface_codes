def decimal_to_base3(n):
    if(n==0):
        return
    r=n%3
    n=n//3
    if(r<0):
        n+=1
    decimal_to_base3(n)
    if(r<0):
        print(r+(3*-1),end="")
    else:
        print(r,end="")
def con(dec):
    if(dec!=0):
        decimal_to_base3(dec)
    else:
        print("0",end="")
dec=int(input())
con(dec)

