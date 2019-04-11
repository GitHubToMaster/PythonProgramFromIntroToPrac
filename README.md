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

### 函数

#### 参数传递

##### 位置实参
> 要求实参的顺序与形参的顺序相同

```python
def describe_pet(animal_type, pet_name):
    """
    显示宠物的信息
    :param animal_type: 动物种类
    :param pet_name: 宠物名称
    :return: None
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +".")

describe_pet('hamster', 'harry')
```

##### 关键字实参
> 每个实参都有变量名和值组成,在传递过程中将名称和值关联起来

注意：使用关键字实参的时候，实参的顺序无关紧要，**务必准确地指定函数定义中的形参名**

```python
def describe_pet(animal_type, pet_name):
    """
    显示宠物的信息
    :param animal_type: 动物种类
    :param pet_name: 宠物名称
    :return: None
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +".")

describe_pet(animal_type='hamster', pet_name='harry')

```

##### 默认值

注意：**在参数中定义默认值的时候，有默认值的参数必须放到没有默认值参数的后面，否则会报出如下错误**
> SyntaxError: non-default argument follows default argument

默认值参数定义以后，Python将会把其他参数当做位置参数进行解析，传递实参的时候仍然需要注意**参数顺序**

```python

def describe_pet2(animal_type="dog", pet_name):
    """
    显示宠物的信息
    :param animal_type: 动物种类
    :param pet_name: 宠物名称
    :return: None
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +".")
```

##### 传递任意数量的实参
> 有时候我们并不知道需要向函数传递多少个参数，此时可以使用*来对参数进行修饰

**在函数中，Python将会把不定数量的参数转换为一个元祖，然后对其进行操作**

```python
def say_hello(*names):
    # Python将会把传递过来的参数创建为一个names元祖
    for name in names:
        print("Hello, " + name)

say_hello("yirufeng", "sivan")

```

###### 使用任意数量的关键字实参
> 当需要接收任意数量的实参，并且预先不知道函数传递给函数的会是什么样的信息，在这种情况下，可将函数编写出能够接受任意数量的键值对-----调用语句提供多少就接受多少

```python
# **user_info 前面有两个星号将会被Python创建为一个字典
# 只有一个星号的时候将会被创建为一个元祖
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

```

#### 函数中修改内容
> 在函数中接收传递过来的列表或字典并对其进行修改都是永久性的

如果需要函数不对列表或字典本身进行修改，可以将列表或字典切片[:]传递给函数，此时函数只会对其副本进行修改

------------

## 第二部分
### 项目2 数据可视化

#### matplotlib
1. 使用plot.plot()绘制折线图
2. 使用plot.scatter()绘制散点图