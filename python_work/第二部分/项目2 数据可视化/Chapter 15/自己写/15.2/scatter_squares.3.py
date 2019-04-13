# 自动计算数据
import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers.", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.tick_params(axis="both", labelsize=16)
# 依次从每个列表中读取一个值来绘制一个点
plt.scatter(x_values, y_values, s=100)

# 设置每个坐标轴的取值范围，四个参数分别对应X轴的最小值和最大值，Y轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])
plt.show()