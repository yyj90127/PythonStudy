def list_sort(list,x,y):
    # 1、将给到的列表根据第x列进行降序排序
    list.sort(key = lambda item:item[x], reverse=True)
    # 2、输出第x列排名前y的行，并给这些行加上排名
    if len(list) <= y:
        for k, line in enumerate(list):
            line.insert(0, k+1)
        return list
    # 3、若第x列的数据在第y行存在重复时，则输出所有重复数据的行，并给这些行加上排名
    else:
        # 获取第y行第x列的值
        num = list[y-1][x]
        # 把第x列的值提取出来并放在一个list中
        new_list = []
        for i in list:
            new_list.append(i[x])
        # 在存放第x列值的列表中统计是否有与第y行值相同的值
        count = new_list.count(num)
        j = new_list.index(num)
        for k, line in enumerate(list[:j + count]):
            line.insert(0, k+1)
        return list[:j + count]


A = [[1,2,1],[2,2,6],[12,3,5],[22,2,4],[2,1,4],[5,4,0]]
print(list_sort(A,-1,5))