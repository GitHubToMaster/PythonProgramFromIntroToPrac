import matplotlib.pyplot as plt
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.title("Square Numbers.", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.tick_params(axis="both", labelsize=10)
plt.axis([1, 5001, 1, 125000000000])
plt.scatter(x_values, y_values, edgecolor='none', s=50, c=y_values, cmap=plt.cm.Blues)
plt.savefig('./1.png', bbox_inches="tight")
