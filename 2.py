s1=input()
s2=input()
count=0
for i in s1:
    if(s2[-1]==i):
        count+=1
print(count)