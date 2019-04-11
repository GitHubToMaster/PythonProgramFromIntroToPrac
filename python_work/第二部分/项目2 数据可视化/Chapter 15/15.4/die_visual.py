from die import Die
import pygal
die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)


# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 绘制直方图对结果进行可视化
hist = pygal.Bar() # 创建一个条形图
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies) # 第1个参数表示要给添加的值指定的标签，第2个参数以列表的形式将出现在图表中的值
hist.render_to_file('die_visual.svg')
