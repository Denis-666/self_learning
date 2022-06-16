
course = " python programming   "
print(course.upper())   #改为大写
print(course.lower())   #改为小写
print(course.title())   #首字母大写
print(course.rstrip()) #把最后 的空格去掉
print(course.find("Pro")) #在string 里面找 Pro 由于 python 是大小写敏感，所以返回 -1？我也不懂
print(course.replace("p", "j")) # 把p 替换成 j
print("pro" in course)  # 在 string 里么找 pro 返回 true，由于 python 是大小写敏感 如果 Pro 会返回 false
print("swift" not in course) # 判否

