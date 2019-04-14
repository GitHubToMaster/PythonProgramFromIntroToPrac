import json

# 获取用户最喜欢的数字并存储到文件中
number = input("Please input your favorite number：")
filename = "fav_num.json"
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

# 从文件中读取用户最喜欢的数字
with open(filename) as f_obj:
    number = json.load(f_obj)
print("I know your favorite number! It's ", number)