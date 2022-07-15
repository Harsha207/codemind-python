def isprime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
    return 1
t=int(input())
for i in range(t):
    n=int(input())
    f,b=n,n
    for i in range(n,0,-1):
        if isprime(i):
            break
    for j in range(n,n+100):
        if isprime(j):
            break
    if (n-i)<=(j-n):
        print(i)
    else:
        print(j)