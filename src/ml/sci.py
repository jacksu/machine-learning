
# coding: utf-8

# In[2]:


import numpy as np
from scipy import linalg
arr = np.array([[1, 2],[3, 4]])
##矩阵行列式
print("矩阵行列式：",linalg.det(arr))
print("矩阵的逆：",linalg.inv(arr))


# In[5]:


#奇异值分解
arr = np.arange(9).reshape((3, 3)) + np.diag([1, 0, 1])
uarr, spec, vharr = linalg.svd(arr)
print(spec)
sarr = np.diag(spec)
svd_mat = uarr.dot(sarr).dot(vharr)
print(svd_mat)
np.allclose(arr,svd_mat)


# In[10]:


##傅里叶变换
##优化
from scipy import optimize
def f(x):
    return x**2 + 10*np.sin(x)
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x)) 
plt.show() 
##bfgs依赖于初始点，有可能得到局部最小
optimize.fmin_bfgs(f, 0)


# In[12]:


optimize.fmin_bfgs(f, 3)


# In[13]:


##全局最优
optimize.basinhopping(f, 0)


# In[15]:


#计算函数的根
#1 只求的一个
root = optimize.fsolve(f, 1)
root


# In[16]:


##曲线拟合
xdata = np.linspace(-10, 10, num=20)
ydata = f(xdata) + np.random.randn(xdata.size)
#假设满足函数f2，然后求a、b
def f2(x, a, b):
     return a*x**2 + b*np.sin(x)
guess = [2, 2]
params, params_covariance = optimize.curve_fit(f2, xdata, ydata, guess)
params


# In[27]:


#统计
a = np.random.normal(size=1000)
bins = np.arange(-4, 5)
print(bins)
histogram = np.histogram(a, bins=bins, normed=True)[0]
print(histogram)
bins = 0.5*(bins[1:] + bins[:-1])
print(bins)
from scipy import stats
#pdf概率密度函数probability density function
b = stats.norm.pdf(bins)
print("pdf:",b)
plt.plot(bins, histogram)
plt.plot(bins, b)
plt.show()
loc, std = stats.norm.fit(a)
print("loc:"+str(loc)+"std:"+str(std))
#中位数
np.median(a)


# In[28]:


#50百分位
stats.scoreatpercentile(a, 50)


# In[29]:


#t检验
a = np.random.normal(0, 1, size=100)
b = np.random.normal(1, 1, size=10)
stats.ttest_ind(a, b)


# In[ ]:
