# 绘制直方图
from die import Die
import pygal
# 创建一个D6
die = Die()

# 投掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    roll_num = die.roll()
    results.append(roll_num)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    # 列表的count()用于统计某个元素在列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 传递要给添加的值指定的标签，还有一个列表，其中包含即将出现在图表中的值
hist.add('D6', frequencies)

# 将图表渲染为一个SVG文件，这种文件的扩展名必须为SVG
hist.render_to_file('die_visual.svg')