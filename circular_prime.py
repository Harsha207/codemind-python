def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
    return 1
def rev(n):
    s=0
    while(n):
        r=n%10
        n=n//10
        s=s*10+r
    return s
n=int(input())
if prime(n) and prime(rev(n)):
    print("circular prime")
elif prime(n):
    print('prime but not a circular prime')
else:
    print('not prime')