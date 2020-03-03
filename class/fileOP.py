
file_name = 'go.text.mp3'
old_name = input('input file name')
index = old_name.rfind('.')
if index > 0:
    postindex  = old_name[index:]
new_name = old_name[:index] + '[备份]' + postindex

# print(new_name)

old_f  = open(old_name, 'rb')
new_f =  open(new_name, 'wb')

while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

old_f.close()
new_f.close()