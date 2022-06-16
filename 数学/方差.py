

data_1  = [15,8,12,21,15,19,15]
data_2 = [13,14,9,18,20,18,16,22]

def 方差(data_1):
    average = 0
    for each_number in data_1:
        average = average + each_number

    average = average / len(data_1)
    print(f'average number : {average}')
    # 得到数组平均数

    total_of_number = len(data_1)
    count_all =0
    number_star_at = 0
    for each_number in data_1:
        count_each = (data_1[number_star_at] - average)**2          
        number_star_at = number_star_at + 1
        count_all = count_all + count_each
    print(f'count_all : {count_all}')


    print(f'方差是 ： {count_all/total_of_number}')




方差(data_2) 
# 方差的意义:反映了数据的离散情况，方差越大，代表每一次数据出现越不稳定。反之，方差越小，数据越稳定。

# 标准差：方差开根号 = 标准差

# 方差和标准差 意义是一样的！