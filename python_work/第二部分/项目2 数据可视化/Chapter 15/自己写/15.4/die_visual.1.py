# 分析结果
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
print(frequencies)