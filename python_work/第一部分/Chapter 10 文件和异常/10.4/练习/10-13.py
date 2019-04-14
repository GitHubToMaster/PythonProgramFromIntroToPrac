# 重构后的代码3
import json

# 如果以前存储了用户名，就加载它
#   否则，就提示用户输入用户名并存储它

def get_sorted_username():
    """
    如果存储了用户名，就获取它
    """
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    提示用户输入用户名
    """
    username = input("What is your name？")
    filename = "username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """
    问候用户，并指出其名字
    """
    username = get_sorted_username()
    option = input("Is your username " + username + " ？(y/n)")
    if option == 'y':
        print("Welcome back, " + username)
    else:
        username = get_new_username()
        print("We'll remermber you when you come back, " + username + "!")

greet_user()