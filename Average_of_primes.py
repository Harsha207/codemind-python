def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if prime(i):
        s.append(i)
d=sum(s)
e=len(s)
print("%.2f"%(d/e))