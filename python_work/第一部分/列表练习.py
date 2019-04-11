places_list = ['东京', '上海', '杭州', '北京', '广州']
print(places_list)



places_list2 = places_list
places_list3 = places_list
places_list.sort()
print(places_list)

places_list2.sort(reverse=True)
print(places_list2)

print(sorted(places_list3))
print(places_list3)
places_list3.reverse()
print(places_list3)

print(min(places_list3))
print(max(places_list3))

list_content = [1, 2, 3, 4]


for i in range(1, 21):
    print(i, end='\t')

number_list = []
for i in range(1, 1000001):
    number_list.append(i)

# for i in number_list:
#     print(i)

print(min(number_list))
print(max(number_list))
print(sum(number_list))

number_list = [1, 2, 3, 4]
odd_number_list = [value for value in number_list if value % 2 == 1]
print(odd_number_list)
