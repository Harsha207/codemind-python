n=int(input())
l=list(map(int,input().split()))
se=int(input())
for i in range(n):
    if l[i]==se:
        print('True')
        break
else:
    print('False')