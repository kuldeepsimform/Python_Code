Arr_Num = int(input())
Number_Arr=input()

NumArr = Number_Arr.split()

d = ""
for i in range(len(NumArr)):
    d+=NumArr[i][-1]
if int(d)%10 == 0:
    print("Yes")
else:
    print("No")