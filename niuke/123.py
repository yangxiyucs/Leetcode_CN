# import  functools
#
# a = [1,3,5,2,3,5,10]
#
# def add(a,b):
#     return a +b
# result = functools.reduce(add, a)
# print(result)

b = [1,32,3,4,8,5]

def func(x):
    return x % 2 == 0

result = filter(func, b)
print(list(result))