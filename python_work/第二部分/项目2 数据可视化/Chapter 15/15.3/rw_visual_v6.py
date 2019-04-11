import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 修改点的数量
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_Numbers = list(range(rw.num_points))
    # 将点的大小修改为1
    plt.scatter(rw.x_values, rw.y_values, edgecolors='none', c=point_Numbers, cmap=plt.cm.Blues, s=1)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()


    keep_running = input("Make another walk? (y/n)\n")
    if keep_running == "n":
        break