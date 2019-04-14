# 创建一个包含文件各行内容的列表
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())