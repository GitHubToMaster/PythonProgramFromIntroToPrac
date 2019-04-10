# PythonProgramFromIntroToPrac
《Python编程：从入门到实践》 学习记录


## 字符串
> 注意:在Python中空白泛指任何非打印字符，如空格，制表符和换行符
```Python
print(nick_name.rstrip()) #去掉昵称右边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
print(nick_name.lstrip()) #去掉昵称左边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
print(nick_name.strip()) #去掉昵称两边的空格字符,不仅包含空格,还包括空白字符(制表符，换行符)
```


## Python之禅
> 在解释器中执行如下命令：
```Python
import this
```
## 列表
> 在Python中可以通过索引-1来访问列表最后的一个元素
```Python
names = ["hello", "world"]
print(names[-1]) #通过索引-1来访问列表最后一个元素
```
### 列表的插入
1. 使用append()方法，向列表的最后一个位置插入元素
2. 使用insert()方法，向列表的指定位置插入元素

```python
motorcycles.append('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

### 列表的删除
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
