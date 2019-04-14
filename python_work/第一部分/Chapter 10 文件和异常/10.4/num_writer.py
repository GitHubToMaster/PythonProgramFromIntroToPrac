# 使用函数dump()将数字列表存储到文件number.json中
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    # 指定两个实参，第一个参数指定要存储的数据，第2个参数指定可用于存储数据的文件对象
    json.dump(numbers, f_obj)