import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.title("Squares", fontsize=24)
plt.xlabel("value", fontsize=15)
plt.ylabel("square", fontsize=15)
plt.tick_params(axis="both", labelsize=20)
plt.plot(input_values, squares, linewidth=5)
plt.show()