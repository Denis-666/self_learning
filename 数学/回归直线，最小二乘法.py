from numpy import average
from sympy import N
#  回归直线与最小二乘法


# y=ax+b
# b是节距
# a是斜率
# y是斜线


data_X = (2002, 2004, 2006, 2008, 2010)
data_Y = (236, 246, 257, 276, 286)

data_XY = {}

for i in range(len(data_X)):
    data_XY.update({i: (data_X[0], data_Y[0])})


print(data_XY.items())

average_X = average(data_X)
average_Y = average(data_Y)


print(average_X,average_Y)

count_for_each_time = 0
count_for_total = 0
for i in range(len(data_X)):
    count_for_each_time = data_X[i]*data_Y[i]
    count_for_total = count_for_total + count_for_each_time

M1 = count_for_total
print(f'全部X和Y相成数,再相加 = M1 : {M1}')


count_for_total = 0
for i in range(len(data_X)):
    count_for_each_time = data_X[i]**2
    count_for_total = count_for_total + count_for_each_time


M2 = count_for_total 
print(f'全部X的平方,再相加 = M2 : {M2}')


n=len(data_X) #一共有多少年的数据需要统计

a = (M1 - (n*average_X*average_Y))/(M2 - n * average_X**2)
print(f'final ,a ba 斜率: {a}')

b = average_Y - a * average_X

print(f'b 节距:{b}')

print (f'故,回归直线是: Y = {a}*X +{b}')


# 预测2012 年 需要粮食 是多少

Y = a * 2012 + b

print(Y)
# 答案 299.2 吨