# def reverse():
#     num = int(input())
#     res=0
#     while num>0:
#       print(num)
#       next = num%10
#       num = int(num/10)
#       res = res*10 +next
#       print(res)
#     print (res)
# reverse()

# num_list = [1, 2, 3, 4, 5]
# print(num_list)
#
# for i in range(len(num_list)):
#     print("i==",i)
#     print("length of num_list", len(num_list))
#     if num_list[i] == 2:
#         num_list.pop(i)
#     else:
#         print(num_list[i])
#
# print(num_list)
#


#改进后
# num_list = [1, 2, 3, 4, 5]
# # print(num_list)
# #
# # for i in range(len(num_list)):
# #     if i >= len(num_list):
# #         break
# #
# #     if num_list[i] == 2:
# #         num_list.pop(i)
# #     else:
# #         print(num_list[i])
# #
# # print(num_list)

#倒入式
# num_list = [1, 2, 3, 4, 5]
# print(num_list)
# 
# for i in range(len(num_list)-1, -1, -1):
#     print("i===",i)
#     print("a[i]===",num_list[1])
#     if num_list[i] == 2:
#         num_list.pop(i)
#     else:
#         print(num_list[i])
#
# print(num_list)
