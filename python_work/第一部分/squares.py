number_list = [1, 2, 3, 4]
number_square_list = []
for number in number_list:
    number_square_list.append(number ** 2)

print(number_list)
print(number_square_list)


# 对于上面的的生成可以采用下面的列表解析公式
squares = [value**2 for value in number_square_list]
print(squares)