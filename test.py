def dictionairy():

    # 声明字典
    key_value ={'600965004': [], '24780002': ['600045002','123213'], '600045002': [], '10011382031': [], '10011402008': []}

    NEW = {}
    b = sorted(key_value.items(), key = lambda item:item[1], reverse=True)
    for i in b:
        NEW[i[0]]=i[1]
    print(NEW)



def main():
    dictionairy()

if __name__=="__main__":
    main()
