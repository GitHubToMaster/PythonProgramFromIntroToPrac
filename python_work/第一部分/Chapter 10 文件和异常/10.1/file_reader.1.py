# 以每次一行的方式检查文件，可对文件对象使用for循环
with open('pi_digits.txt') as file_object:
    for line in file_object:
            print(line)