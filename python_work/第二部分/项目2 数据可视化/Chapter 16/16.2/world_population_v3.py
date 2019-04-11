import json
# from pygal.i18n import COUNTRIES # 这行代码不可以解决
from pygal_maps_world import i18n


for country_code in sorted(i18n.COUNTRIES.keys()):
    print(country_code, i18n.COUNTRIES[country_code])

# 将数据加载到一个列表中
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)


# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ": " +  str(population))