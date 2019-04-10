cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  #按照字母顺序升序排序,会对列表进行永久性修改
print(cars)
cars.sort(reverse=True)  #按照字母顺序降序排序，会对列表进行永久性修改
print(cars)

cars2 = ['bmw', 'audi', 'toyota', 'subaru']
## 进行临时性排序
print(sorted(cars2))
print(sorted(cars2, reverse=True))
print(cars2)

## 对列表进行反转：倒着打印列表，
cars3 = ['bmw', 'audi', 'toyota', 'subaru']
cars3.reverse()  #永久性的修改列表中元素的顺序，对列表中各个元素进行反转
print(cars3)