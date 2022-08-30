s=input()
n=input()
f=0
for i in range(len(s)):
    if n==s[i]:
        f=1
        break
if f==1:
    print('True')
    print(i)
else:
    print('False')