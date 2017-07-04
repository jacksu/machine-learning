#encoding=utf8
import numpy as np

# 定义一维数组
a = np.array([2, 0, 1, 5, 8, 3])
print u'原始数据:', a

#输出最大、最小值及形状
print u'最小值:', a.min()
print u'最大值:', a.max()
print u'形状', a.shape

# 数据切片
print u'切片操作:'
# [:-2]后面两个两个值不取
print a[:-2]
#[-2:]表示后往前数两个数字，获取数字至结尾
print a[-2:]
#[:1]表示从头开始获取，获取1个数字
print a[:1]

# 排序
print type(a)
print a.dtype
a.sort()
print u'排序后:', a


#二维数组操作


c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

# 获取值
print u'形状:', c.shape
print u'获取值:', c[1][0]
print u'获取某行:'
print c[1][:]
print u'获取某行并切片:'
print c[0][:-1]
print c[0][-1:]

#获取具体某列值
print u'获取第3列:'
#np.newaxis增加一个新维度
print c[:,np.newaxis, 2]


#函数
#sin
print np.sin(np.pi/6)
print np.sin(np.pi/2)
print np.tan(np.pi/2)

print np.arange(0,4)
