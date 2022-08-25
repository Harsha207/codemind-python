n1=int(input())
n2=int(input())
s=n1+n2
p=s
for i in range(1,11):
    p+=1
    c=0
    for j in range(1,p+1):
        if p%j==0:
            c+=1
    if c==2:
        print(p-s)
        break