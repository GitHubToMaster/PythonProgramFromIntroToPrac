def describe_pet(animal_type, pet_name):
    """
    显示宠物的信息
    :param animal_type: 动物种类
    :param pet_name: 宠物名称
    :return: None
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +".")

describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet2(pet_name, animal_type="dog", ):
    """
    显示宠物的信息
    :param animal_type: 动物种类
    :param pet_name: 宠物名称
    :return: None
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +".")

describe_pet2("wilson", "dog")



def say_hello(*names):
    print(type(names))
    for name in names:
        print("Hello, " + name)

say_hello("yirufeng", "sivan")


def param_test(**test):
    print(type(test))

param_test()


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)