# 给点着色
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=15, edgecolor='none', 
                                        c=point_numbers, cmap=plt.cm.Blues)
    # 下面这行代码这里最好不要用y_value作为颜色，因为y_values有可能重复
    # plt.scatter(rw.x_values, rw.y_values, s=15, edgecolor='none', c=rw.y_values, cmap=plt.cm.Blues)
    plt.show()


    keep_running = input("Make another walk? (y/n)：")
    if keep_running == 'n':
        break