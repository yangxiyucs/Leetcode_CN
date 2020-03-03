import re

#result = re.match(正则表达式,需要处理的字符串)
# result = re.match(r"[hH]ello","Hello world")
# ret  =re.match(r"\d{3,4}-?\d{8}","0532-12345678").group()
email = input("请输入您的邮箱地址")
ret  =re.match(r"[a-zA-Z_0-9]{4,20}@163\.com",email)

if ret:
    print("邮箱合法")
else:
    print("邮箱不合法")

