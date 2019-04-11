import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_Numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, edgecolors='none', c=point_Numbers, cmap=plt.cm.Blues, s=15)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()


    keep_running = input("Make another walk? (y/n)\n")
    if keep_running == "n":
        break