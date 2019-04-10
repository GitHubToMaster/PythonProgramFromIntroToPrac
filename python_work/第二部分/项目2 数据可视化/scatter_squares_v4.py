import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# 由于散点图中的每个点都是蓝色的点，黑色轮廓，所以可以去掉轮廓
plt.scatter(x_values, y_values, s=2, edgecolor=None, c="red")
plt.scatter(x_values, y_values, s=2, edgecolor=None, c=(0.5, 0.4, 0.8))
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)

# 设置X轴和Y轴的取值范围，X轴取值范围设置为0-1100，Y轴取值范围设置为0-1100000
plt.axis([0, 1100, 0, 1100000])



plt.show()