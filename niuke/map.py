n = int(input())
dic = {}
for i in range(n):
    line = input().split()
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key,0)+value
for each in dic:
    print(each, dic[each])