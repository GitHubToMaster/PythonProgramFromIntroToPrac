# PythonProgramFromIntroToPrac
《Python编程：从入门到实践》 学习记录

## 第一部分


### 字符串
> 注意:在Python中空白泛指任何非打印字符，如空格，制表符和换行符
```Python
print(nick_name.rstrip()) #去掉昵称右边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
print(nick_name.lstrip()) #去掉昵称左边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
print(nick_name.strip()) #去掉昵称两边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
```


### Python之禅
> 在解释器中执行如下命令：
```Python
import this
```
### 列表
> 在Python中可以通过索引-1来访问列表最后的一个元素
```Python
names = ["hello", "world"]
print(names[-1]) #通过索引-1来访问列表最后一个元素
```
#### 列表的插入
1. 使用append()方法，向列表的最后一个位置插入元素
2. 使用insert()方法，向列表的指定位置插入元素

```python
motorcycles.append('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

#### 列表的删除
> 列表的删除可以通过Python自带的del语句 以及 pop() 或 remove() 对元素进行删除

1. 通过del语句进行删除
2. 通过remove()进行删除 **只删除找到的第一个元素**
3. 通过pop()删除最后一个元素
4. 通过pop(index)删除给定位置的元素


```python
motorcycles = ['honda', 'honda', 'yamaha', 'suzuki']
del motorcycles[0] #使用删除语句来删除特定元素
print(motorcycles.pop(0)) #通过pop删除给定索引位置处的元素
print(motorcycles.pop()) #如果不给元素默认删除最后一个
motorcycles.remove('yamaha') #只删除找到的第一个元素

```

#### 列表的排序
1. 通过列表的sort()函数来对列表进行永久性排序
2. 通过sorted(列表)来对列表进行临时性排序
3. 通过列表的reverse()来对列表进行永久逆序改变

```python

places_list = ['东京', '上海', '杭州', '北京', '广州']
places_list.sort() #对列表进行升序排列
places_list.sort(reverse=True) #对列表进行逆序排列

# 打印对列表临时排序后的结果，此时places_list并没有变
print(sorted(places_list))

# 对列表逆序输出
places_list.reverse()
print(places_list)

```

#### 对数字列表进行统计
```python
list_content = [1, 2, 3, 4]
print(min(list_content))
print(max(list_content))
print(sum(list_content))

```

#### 列表解析
> 列表解析，也叫列表生成式

[列表要赋的值 迭代列表 条件]

#### 列表的复制
> 采用切片的形式复制列表

```python
food_list = ['chicked', 'burger']
your_food_list = food_list[:]

my_food_list = food_list # 此时两个变量将会指向同一个列表

```

### 元祖


#### 与列表的区别
1. 列表适合用于可能变化的数据集
2. 元祖中的元素是不可变的

> 如果想要修改元祖中的元素，可以尝试重新定义一个元祖并赋值


### if条件语句
**Python并不要求if-elif结构后面必须有else代码块**



### 字典

#### 字典中添加键值对
```python
alien_0 = {'color' : 'green', 'points' : 5}
alien_0['number'] = 10
```

#### 删除字典中的键值对
> 使用del语句时，必须指定字典名和要删除的键
```python
alien_0 = {'color' : 'green', 'points' : 5}
del alien_0['x_position']
```


#### 定义一个空字典
```python
number_dict = {}
```


#### 字典的遍历

##### 遍历字典中所有的键值对
> user_0.itens() 每次迭代会返回一个键值对组成的元祖
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for item in user_0.items():  #每次会将字典中的一个键值对组成一个元祖返回
    print(item)
    print(type(item))
```

##### 遍历字典中所有的键


```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key in user_0.keys():
    print(key)
```

**遍历字典的时候会默认遍历字典中的键**
> 例如下面的代码等同于上面的代码
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key in user_0:
    print(key)
```

##### 按顺序遍历字典中的所有键
> 获取字典的元素的时候，获取顺序是不可预测的，可以采用如下方案按照特定顺序返回元素
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key in sorted(user_0.keys()):
    print(key)

for key, value in sorted(user_0.items()):
    print(key, value)
```


##### 遍历字典中所有的值
> 如果希望去除字典中重复的值，可以将值转换为set集合，再进行遍历
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for value in user_0.values():
    print(value)
   
# 去掉字典中重复的值并进行遍历
for value in set(user_0.values()):
    print(value)

```

### while循环

**for循环是一种遍历列表的有效方式，但是在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素，如果要在遍历的同时进行修改可以使用while循环**

------------

## 第二部分
### 项目2 数据可视化

#### matplotlib
1. 使用plot.plot()绘制折线图
2. 使用plot.scatter()绘制散点图