n=int(input())
m=n
s=0
while(m>0):
    r=m%10
    m//=10
    f=1
    for i in range(r,1,-1):
        f*=i
    s+=f
if(n==s):
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")