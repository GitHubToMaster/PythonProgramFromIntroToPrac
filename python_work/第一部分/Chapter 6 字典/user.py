user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'other': 'fermi'
}

# 使用for循环遍历字典
for key, value in user_0.items():
    print(key + ":" + value)

for item in user_0.items():  #每次会将字典中的一个键值对组成一个元祖返回
    print(item)
    print(type(item))

for key in user_0.keys():
    print(key)

for key in user_0:
    print(key)



for key, value in sorted(user_0.items()):
    print(key, value)

for key in sorted(user_0.keys()):
    print(key)



for value in user_0.values():
    print(value)

for value in set(user_0.values()):
    print(value)

