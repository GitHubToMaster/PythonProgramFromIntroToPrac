import csv
filename = '../sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  #创建于该文件相关联的阅读器对象
    header_row = next(reader)  #将阅读器对象传递给它时，将会返回文件中的下一行，只调用一次，所以得到的是文件的第一行
    print(header_row)
    # header_row = next(reader)
    # print(header_row)


# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)