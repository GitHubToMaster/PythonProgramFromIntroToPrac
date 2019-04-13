import matplotlib.pyplot as plt
x_value = [1, 2, 3, 4, 5]
y_value = [x**3 for x in x_value]
plt.tick_params(axis="both", labelsize=15)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.scatter(x_value, y_value, s=100)
plt.show()