# 自动保存图表
import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers.", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.tick_params(axis="both", labelsize=16)

# 我们将参数c设置成一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射
# 这些代码将y值较小的元素显示为浅蓝色，将y值较大的元素显示为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
# 设置每个坐标轴的取值范围，四个参数分别对应X轴的最小值和最大值，Y轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])

# 第1个实参指定要以什么样的文件保存图表，这个文件将存储到scatter_squares.py所在的目录
# 第2个实参指定将图表多余的空白区域裁减掉，如果要保留图表多余的空白区域，可以省略这个实参
plt.savefig('squares_plot.png', bbox_inches='tight')
