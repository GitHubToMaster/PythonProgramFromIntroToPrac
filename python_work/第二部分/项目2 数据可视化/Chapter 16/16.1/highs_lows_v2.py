# 为了让文件头数据更容易理解，打印文件头以及其位置
import csv
filename = '../sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, content in enumerate(header_row):  #通过enumerate获取对应的索引以及其值
        print(index, content)


