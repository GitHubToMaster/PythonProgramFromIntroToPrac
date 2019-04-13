from random import choice
import matplotlib.pyplot as plt
class RandomWalk():
    def __init__(self, point_numbers=5000):
        self.point_numbers = point_numbers
        # 从原点开始进行随机漫步
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        while len(self.x_values) < self.point_numbers:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            next_x_values = self.x_values[-1] + x_step
            next_y_values = self.y_values[-1] + y_step
            self.x_values.append(next_x_values)
            self.y_values.append(next_y_values)


rw = RandomWalk(50000)
rw.fill_walk()
point_nums = list(range(rw.point_numbers))
# 调整屏幕尺寸以及分辨率
plt.figure(figsize=(10, 6), dpi=128)
plt.title("Random Walk.", fontsize=24)
plt.xlabel("x_values", fontsize=14)
plt.ylabel("y_values", fontsize=14)
plt.tick_params(axis="both", labelsize=15)
plt.scatter(rw.x_values, rw.y_values, edgecolor='none', 
                c=point_nums ,s=1, cmap=plt.cm.Blues)
plt.scatter(0, 0, edgecolor='none', s=100, c='green')
plt.scatter(rw.x_values[-1], rw.y_values[-1], edgecolor='none', s=100, c='red')
# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
