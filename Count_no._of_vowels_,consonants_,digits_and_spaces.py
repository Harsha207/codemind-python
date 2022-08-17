s=input()
vc=0
cc=0
dc=0
ws=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vc+=1
    elif i.isdigit():
        dc+=1
    elif i==' ':
        ws+=1
    else:
        cc+=1
print('Vowels:',vc)
print('Consonants:',cc)
print('Digits:',dc)
print('White spaces:',ws)