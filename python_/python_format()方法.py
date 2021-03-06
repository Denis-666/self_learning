'''
字符串类型格式化采用format()方法，基本使用格式是：
<模板字符串>.format(<逗号分隔的参数>)
调用format()方法后会返回一个新的字符串，参数从0 开始编号。
'''


print("{}{}{}".format("圆周率是",3.1415926,"..."))
# Out[11]: '圆周率是3.1415926...'
 
print("圆周率{{{1}{2}}}是{0}".format("无理数",3.1415926,"..."))
# Out[12]: '圆周率{3.1415926...}是无理数'



'''
<填充>
指<宽度>内除了参数外的字符采用什么方式表示，默认采用空格，可以通过<填充>更换。
'''

s = "PYTHON"
 
print("{0:30}".format(s))
# Out[17]: 'PYTHON                        '
 
print("{0:>30}".format(s))
# Out[18]: '                        PYTHON'
 
print("{0:*^30}".format(s))
# Out[19]: '************PYTHON************'
 
print("{0:-^30}".format(s))
# Out[20]: '------------PYTHON------------'
 
print("{0:3}".format(s))
# Out[21]: 'PYTHON'







'''
逗号（，）

<格式控制标记>中逗号（，）用于显示数字的千位分隔符，例如：
'''

print("{0:-^20,}".format(1234567890))
# Out[24]: '---1,234,567,890----'
 
print("{0:-^20}".format(1234567890)) #对比输出
# Out[25]: '-----1234567890-----'
 
print("{0:-^20,}".format(12345.67890))
# Out[26]: '----12,345.6789-----'


'''
 <.精度>
表示两个含义，由小数点（.）开头。对于浮点数，精度表示小数部分输出的有效位数。
对于字符串，精度表示输出的最大长度。
'''

print("{0:.2f}".format(12345.67890))
# Out[29]: '12345.68'
 
print("{0:H^20.3f}".format(12345.67890))
# Out[30]: 'HHHHH12345.679HHHHHH'
 
print("{0:.4}".format("PYTHON"))
# Out[31]: 'PYTH'



'''
<类型>

表示输出整数和浮点数类型的格式规则。对于整数类型，输出格式包括6 种：

b: 输出整数的二进制方式；
c: 输出整数对应的 Unicode 字符；
d: 输出整数的十进制方式；
o: 输出整数的八进制方式；
x: 输出整数的小写十六进制方式；
X: 输出整数的大写十六进制方式；

'''

print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
# Out[32]: '110101001,Ʃ,425,651,1a9,1A9'


'''
对于浮点数类型，输出格式包括4 种：
e: 输出浮点数对应的小写字母 e 的指数形式；
E: 输出浮点数对应的大写字母 E 的指数形式；
f: 输出浮点数的标准浮点形式；
%: 输出浮点数的百分形式。
浮点数输出时尽量使用<.精度>表示小数部分的宽度，有助于更好控制输出格式。
'''

print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
# Out[33]: '3.140000e+00,3.140000E+00,3.140000,314.000000%'
 
print("{0:.2e},{0:.2E},{0:.2f},{0:.2%}".format(3.14))
# Out[34]: '3.14e+00,3.14E+00,3.14,314.00%'

