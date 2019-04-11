import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.title('square', fontsize=30)
plt.xlabel('x label', fontsize=24)
plt.ylabel('y label', fontsize=24)
plt.tick_params(axis='both', labelsize=20)
plt.plot(squares, linewidth=15)
plt.show()