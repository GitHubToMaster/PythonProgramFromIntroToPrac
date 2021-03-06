# 增加点数
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, edgecolor='none', 
                                        c=point_numbers, cmap=plt.cm.Blues)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # 下面这行代码这里最好不要用y_value作为颜色，因为y_values有可能重复
    # plt.scatter(rw.x_values, rw.y_values, s=15, edgecolor='none', c=rw.y_values, cmap=plt.cm.Blues)
    plt.show()


    keep_running = input("Make another walk? (y/n)：")
    if keep_running == 'n':
        break