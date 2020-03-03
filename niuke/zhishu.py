num = int(input())
list1 = []
if num !=1:
    for i in range(2, num):
        while num % i == 0:
            num /= i
            list1.append(str(i))

print(" ".join(list1))

