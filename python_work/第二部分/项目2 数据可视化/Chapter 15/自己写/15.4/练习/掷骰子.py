from random import randint
import pygal
class Die():
    def __init__(self, sides_num=6):
        self.sides_num = sides_num
    
    def roll(self):
        return randint(1, self.sides_num)

die = Die()
results = []
for i in range(1000):
    results.append(die.roll())


# 统计次数
frequencies = []
for i in range(1, die.sides_num+1):
    frequency = results.count(i)
    frequencies.append(frequency)

# 绘制图进行分析
hist = pygal.Bar()
hist.title = "投掷1次D6"
hist.x_title = "投掷1次产生的值"
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.y_title = "次数"
hist.add('D6', frequencies)
hist.render_to_file('die_1.svg')