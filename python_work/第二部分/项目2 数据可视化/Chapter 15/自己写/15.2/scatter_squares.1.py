# 设置输出的样式，使其更有趣，添加标题，并给轴加上标签，并确保所有文本都能够看清
import matplotlib.pyplot as plt
plt.scatter(2, 4, s=200)
# 设置标题并给轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of value", fontsize=14)
# 设置刻度标记
"""
which一共3个参数['major' ， 'minor'，'both'] 
默认是major表示主刻度，后面分布为次刻度及主次刻度都显示。
"""
plt.tick_params(axis="both", labelsize=14, which="minor")
plt.show()