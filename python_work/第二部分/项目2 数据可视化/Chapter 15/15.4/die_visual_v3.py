from die import Die
import pygal
die_1 = Die()
die_2 = Die(10)


results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)


# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 绘制直方图对结果进行可视化
hist = pygal.Bar() # 创建一个条形图
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results of rolling two D6 dice 50000 times."
hist.y_title = "Result"
hist.add('D6 + D6', frequencies) # 第1个参数表示要给添加的值指定的标签，第2个参数以列表的形式将出现在图表中的值
hist.render_to_file('die_visual3.svg')
