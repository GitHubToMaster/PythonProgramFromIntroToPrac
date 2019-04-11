# 在图标中添加日期
import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = '../sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')  # dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
# 设置图片格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()  # 通过该方法可以绘制斜的日期标签，以免它们彼此重叠
plt.tick_params(axis="both", labelsize=16)
plt.show()


