s  = input()
zoo = s[0]
c = 0
if len(s) <=20:
    for i in range(len(s)):
        if(zoo == s[i]):
            c+=1
        else:
            break

if(len(s[c:]) == 2 * c ):
    print("Yes")
else:
    print("No")