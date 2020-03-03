str1 = set(list(input()))
num = 0
for i in str1:
 if(0<= ord(i) and ord(i) <=127):
    print(i)
    print(ord(i))
    num+=1
print(num)
