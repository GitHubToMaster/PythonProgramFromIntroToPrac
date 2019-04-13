# 投掷骰子
from die import Die
import pygal
# 创建一个D6
die = Die()

# 投掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    roll_num = die.roll()
    results.append(roll_num)

print(results)