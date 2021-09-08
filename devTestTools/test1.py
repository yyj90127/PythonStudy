import random
import string

def get_str():
    # 26个字母的大小写
    str = string.ascii_letters
    # 0-9数字
    str = string.digits
    # 26个字母大写
    str = string.ascii_uppercase
    # 26个字母小写
    str = string.ascii_lowercase
    # 符号
    str = string.punctuation

    return str


def get_random():
    # 获取x-y中的随机整数
    a = random.randint(7,10)
    b = random.randint(2,5)
    # 在指定的字符串中随机取x个字符
    A = random.sample(string.digits,a)
    B = random.sample(string.ascii_lowercase,b)

    return A,B



for i in range(0,1):
    A,B = get_random()
    str = get_str()
    email = ''.join(A)+'@'+''.join(B)+'.com'
    print(email)