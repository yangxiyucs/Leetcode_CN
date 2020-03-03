num = (input())
num1 = num.split(".")
print(num1)
if(int(num1[1]) >= 5):
    print(int(num1[0])+1)
else:
    print(int(num1[0]))
