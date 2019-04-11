import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# 由于散点图中的每个点都是蓝色的点，黑色轮廓，所以可以去掉轮廓
# plt.scatter(x_values, y_values, s=2, edgecolor=None, c="red")
# 通过红绿蓝三原色配置颜色
# plt.scatter(x_values, y_values, s=2, edgecolor=None, c=(0.5, 0.4, 0.8))
# 使用颜色映射，也就是渐变色
plt.scatter(x_values, y_values, s=40, edgecolor=None, c=y_values, cmap=plt.cm.Blues)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)

# 设置X轴和Y轴的取值范围，X轴取值范围设置为0-1100，Y轴取值范围设置为0-1100000
plt.axis([0, 1100, 0, 1100000])


# 将图显示出来
plt.show()

# 保存图,第一个参数指定储存的路径以及文件名称，第2个参数指定将图表多余的空白去掉
# plt.savefig("squares_plo1t.png", bbox_inches="tight")
