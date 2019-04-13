import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Numbers", fontsize=14)
plt.tick_params(axis="both", labelsize=15)
plt.plot(input_values, squares, linewidth=15)
plt.show()