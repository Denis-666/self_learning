

# 关于 用* 去 解 包

numbers = [1,2,3,5,6,78,9,0,8,99]

first, *middle,last = numbers

# print(middle)




#  关于给 list 增 改
# 肉眼可见的功能，不懂再查
# 还有些 让元组排序的功能 我就不写了


letters = ['a','b','c']

letters.append('d')
print(letters)

letters.insert(0, '-')
print(letters)

letters.remove('a') #remove 就是 要谁死，就谁死！ 精准打击
print(letters)

letters.pop(0) #pop 就是让第几个 消失 pop 一声 蒸发了!!
print(letters)

letters.clear()
print(letters)


