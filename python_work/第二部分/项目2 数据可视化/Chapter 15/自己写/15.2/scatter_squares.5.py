# 修改数据点的颜色
import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers.", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.tick_params(axis="both", labelsize=16)
# 依次从每个列表中读取一个值来绘制一个点
# plt.scatter(x_values, y_values, s=100, edgecolor='none', c='red')
# 颜色是一个元祖，分别表示红绿蓝的分量，值越接近1，颜色越浅
plt.scatter(x_values, y_values, s=100, edgecolor='none', c=(0,0,0.8))
# 设置每个坐标轴的取值范围，四个参数分别对应X轴的最小值和最大值，Y轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])
plt.show()