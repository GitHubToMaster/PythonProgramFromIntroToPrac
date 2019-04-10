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
## 通过值删除元素
a = motorcycles.remove('yamaha')
print(motorcycles)


## 通过索引删除元素
del motorcycles[0] #使用删除语句来删除特定元素
print(motorcycles)

print(motorcycles.pop(0)) #通过pop删除给定索引位置处的元素
print(motorcycles.pop()) #如果不给元素默认删除最后一个
print(motorcycles)


list1 = ['hello', 'hello']
list1.remove('hello')
print(list1)


list2 = [1, 2, 3, 4]
list2.insert(2, 6)
print(list2)