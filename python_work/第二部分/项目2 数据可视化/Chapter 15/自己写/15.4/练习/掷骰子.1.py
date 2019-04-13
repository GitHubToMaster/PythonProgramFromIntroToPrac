from random import randint
import pygal
class Die():
    def __init__(self, sides_num=6):
        self.sides_num = sides_num
    
    def roll(self):
        return randint(1, self.sides_num)

die = Die()
die_2 = Die(10)
results = []
for i in range(50000):
    results.append(die.roll() + die_2.roll())


# 统计次数
frequencies = []
for i in range(2, die.sides_num+1+die_2.sides_num):
    frequency = results.count(i)
    frequencies.append(frequency)

# 绘制图进行分析
hist = pygal.Bar()
hist.title = "投掷1次D6 和 1次D10"
hist.x_title = "投掷2次产生的值"
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
hist.y_title = "次数"
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_2.svg')