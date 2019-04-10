#coding:utf-8
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表中插入元素
motorcycles.append('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 从列表中删除元素
a = motorcycles.remove('yamaha')
print(motorcycles)
del motorcycles[0] #使用删除语句来删除特定元素
print(motorcycles)
print(a)

