# 使用scatter()绘制一系列点
import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.title("Square Numbers.", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.tick_params(axis="both", labelsize=16)
# 依次从每个列表中读取一个值来绘制一个点
plt.scatter(x_values, y_values, s=100)
plt.show()