#coding=utf-8
name = "a lovelace"
print(name.title()) #将字符串中的每个单词首字母大写，其他字母小写

name = "Sivan Wu"
print(name.upper()) #将字符串全部转换为大写
print(name.lower()) #将字符串全部转换为小写

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())


nick_name = " yirufeng "
print(nick_name.rstrip()) #去掉昵称右边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
print(nick_name.lstrip()) #去掉昵称左边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
print(nick_name.strip()) #去掉昵称两边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)

