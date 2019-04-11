# import matplotlib.pyplot as plt
# x_values = list(range(1, 6))
# y_values = [x**3 for x in x_values]
# plt.title("Square", fontsize=24)
# plt.xlabel("Value", fontsize=15)
# plt.ylabel("The value of square:", fontsize=15)
# plt.tick_params(axis="both", labelsize=20, which="major")
# plt.scatter(x_values, y_values)
# plt.show()


# import matplotlib.pyplot as plt
# x_values = list(range(1, 5001))
# y_values = [x**3 for x in x_values]
# plt.title("Square", fontsize=24)
# plt.xlabel("Value", fontsize=15)
# plt.ylabel("The value of square:", fontsize=15)
# plt.tick_params(axis="both", labelsize=20, which="major")
# plt.scatter(x_values, y_values)
# plt.show()





import matplotlib.pyplot as plt
x_values = [x for x in range(1, 5001)]
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, cmap=plt.cm.Blues, edgecolors=None, c=y_values)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("The Cube of Value", fontsize=18)
plt.tick_params(axis="both", labelsize=20, which="major")
plt.show()