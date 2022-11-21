n=int(input())
l=[0,1,2,5,6,8,9]
c=0
k=6
i=10

if((len(l)-1)<n):
    while(k==n):
        s=str(i)
        print(s)
        for j in s:
            if int(j) in l:
                c+=1
        if(len(s)==c):
            l.append(int(i))
            k+=1
        i+=1
else:
    print(l[n-1])

print(l)


