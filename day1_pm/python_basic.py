
# coding: utf-8

# # 基本数据类型

# ## 1. 数字
# Python可以处理任意大小的整数，当然包括负整数，`1，100，-1000，0` ceshi
# 
# 常见操作符：
# - 加法：+
# - 减法：-
# - 乘法：*
# - 除法：/ （python3中除法都是以浮点型进行运算，即使两个数都是整数）
# - 取余：//

# In[7]:


6/5


# In[6]:


1+100-1000+4


# In[2]:


2.1 + 4.3 * 54


# In[3]:


print(type(5))
print(type(2))
5/2


# ## 2. 字符串
# 字符串是以单引号`'`或双引号`"`括起来的任意文本，多行文本用`''' '''`，对于特殊字符用`\`进行转意

# In[10]:




# In[9]:


print('hello world!') #普通字符
print('I\'m learning "Python".') #转移字符，' 和 回车
print(r"I'm learning 'Python'.") #转移字符，用r开头
print('''多行文本开始：
第一行，
第二行，




。。。''') # 多行文本


# ## 3. 布尔值
# 布尔值只有True、False两种值

# In[11]:


True


# In[12]:


False


# In[7]:


if True:
    print('this is Ture')
if False:
    print('nothing...')


# ## 4. 变量
# 
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头，

# In[15]:


# var = 0
# print(type(var))
# Var = 'fasdf'
# print(type(Var))
# var_1 = 111
# _var2 = 222

2fdsa = 333 # 错误，不能以数字开头


# python是动态语言，因此不会像C语言那样，每个变量有固定的数据类型

# In[16]:


pi = 3.1415926
type(pi)


# In[17]:


pi = 'pi value is 3.1415926'
type(pi)


# ## 5. 列表list & 元组tuple
# 列表是python内置的数据类型，一种有序的集合，以中括号开始和结束，一个列表中可以包含所中数据类型，甚至可以嵌套list

# In[18]:


geo_institute = ['地理所','遥感所','湖泊所']
geo_institute


# In[19]:


geo_institute = ['地理所', '遥感所', '湖泊所', 11, 21, 3.14, True] #多种数据类型
geo_institute


# In[23]:


geo_institute = ['地理所', '遥感所', '湖泊所', [11, 12, 3.14], True, False] #嵌套list
geo_institute


# ### 5.1 访问元素
# 

# In[25]:


len()
geo_institute


# In[27]:


geo_institute[6] #按下标访问
# geo_institute[100] #错误，下标越界


# In[29]:


geo_institute[-6] #倒序访问


# In[30]:


geo_institute[3]


# In[32]:


geo_institute[1:3] # 切片，左闭右开


# In[33]:


a=[1,2,3,4,5,6,7,8,9]


# In[37]:


a[0:8:3]


# In[17]:


geo_institute[0:6:2] # 步长切片


# In[38]:


geo_institute


# In[41]:


# 嵌套数组的获取
geo_institute[3][2]


# ### 5.2 基本操作
# 

# In[42]:


geo_institute


# In[43]:


# 修改元素
geo_institute[2] = '寒旱所'
geo_institute


# In[44]:


# 删除元素
print('原始：', geo_institute)
geo_institute.pop()  # 删除最后一个元素


print('删除最后一个元素：', geo_institute)
geo_institute.pop(0)  # 删除第一一个元素
print('删除第一个元素：', geo_institute)


# In[46]:


# 添加元素
geo_institute.insert(0, '地理所') # 任意位置添加元素
print(geo_institute)
geo_institute.append('地理所') # 任意位置添加元素
print(geo_institute)
# 末尾添加元素

# geo_institute.


# In[47]:


# 判断元素是否在列表中
'遥感所' in geo_institute


# In[48]:


'物理所' in geo_institute


# In[50]:


a=[1,1,1,1,2,3]
a


# ### 5.3元组
# tuple和list非常类似，但是tuple一旦初始化就不能修改

# In[53]:


tuple_institute = ('地理所', '遥感所', '湖泊所')
tuple_institute.append(123) #错误


# In[52]:


tuple_institute


# In[54]:


tuple_institute[0] = 3.14 #错误，不能修改值


# ## 6. 字典dict & 集合set
# dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。dict内部存放的顺序和key放入的顺序是没有关系的。
# 
# 和list比较，dict有以下几个特点：
# 
# 1. 查找和插入的速度极快，不会随着key的增加而变慢；
# 2. 需要占用大量的内存，内存浪费多。
# 
# 而list相反：
# 
# 1. 查找和插入的时间随着元素的增加而增加；
# 2. 占用空间小，浪费内存很少。
# 
# dict是用空间来换取时间的一种方法。

# In[59]:


dict_institute={
    1:'北京市',
    '遥感所':'北京市',
    '湖泊所':'南京市',
    '寒旱所':'兰州市'
}


# In[60]:


dict_institute[1]


# In[28]:


dict_institute['湖泊所'] = 'nanjing'
dict_institute


# ### set
# 
# 可以看成数学意义上的无序和无重复元素的集合

# In[29]:


s = set([1,2,3])
s


# In[64]:


a = [1，2]


# In[63]:


# 去重
s = set([1, 1， 3, 3])
s


# ----

# # 条件判断&循环

# ## 1. 条件判断

# In[67]:


a = True
a


# In[74]:


age = float(input())
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
elif age > 60:
    print('old')
else:
    print('kid')


# ``` python
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
# ```

# ## 2. 迭代

# In[83]:


# 列表循环
list_institute = range(100000)
for index, item in enumerate(list_institute):
#     print function
#     a = index/len(list_institute)*100
#     print(index, item)
    pass


# In[87]:


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum += x
    sum = sum + x
print(sum)


# In[88]:


# 字典循环
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for k,v in d.items():
    print(k, v)


# ---
# 
# # 函数
# 
# ## 1.函数的调用

# In[2]:


abs(-91)


# In[3]:


int('123')


# ## 2.函数的定义

# In[89]:


def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

my_abs(-10)


# In[90]:


# 返回多个值
def my_abs(x):
    "放回原始值和绝对值"
    if x>=0:
        return x, x
    else:
        return x, -x
    
my_abs(100)


# ## 3.函数的参数
# 
# python有四种参数传递方式：
# - 位置参数
# - 默认参数
# - 可变参数
# - 关键字参数
# 
# 上面的例子都是位置参数

# In[95]:


#默认参数 
def person(name, gender, age=20, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

person('tom', 'male', age=30, city='shagnhai')


# In[97]:


#可变参数 , 在参数数量未知的情况下
def person(name, gender, age=20, city='beijing', *food):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print('喜欢的食物：',','.join(food))

person('tom', 'male', 18, 'shenzhen', *['苹果','荔枝', '百香果','xiangjiao'])


# In[98]:


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# ## 4. 列表生成式
# 计算几个数字的平方

# In[99]:


# 传统方式
def cal_square(x):
    return x*x

for item in range(1,11):
    print(cal_square(item))


# In[100]:


# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
lc = [x * x for x in range(1, 11)]
lc


# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

# In[103]:


[x * x for x in range(1, 11) if x % 2 == 0]


# ## 5.生成器
# 列表生成式一次性把所有数据都生成完，并保存到内存中，在大数据量的情况下，使用列表生成式将非常消耗内存。
# 
# python有一种更高效的方式：生成器，每次执行时动态计算，这种一边循环一边计算的机制

# In[117]:


# 生成器定义
g = (x * x for x in range(10))
g


# In[118]:


# 取值
next(g)


# In[119]:


for item in g:
    print(item)


# ## 6. map函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# In[120]:


def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[122]:


r


# In[121]:


list(r)


# ## 7. 匿名函数
# 不需要显式地定义函数

# In[123]:


f = lambda x: x * x
list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 
# #     -----------------模块----------------
# 
# python有非常多现有的包库，可以直接使用，不用我们再次开发，重复造轮子。
# - 标准库（python官方自带）
# - 第三方库
# 
# 标准库只要安装完毕，这些模块就可以立刻使用，第三方库需要手动安装，比如numpy、matplotlib...

# ## 1. 标准库

# In[124]:


import math


# In[133]:


import numpy as np


# In[134]:


np.abs(-123)


# In[125]:


math.sqrt(123)


# In[35]:


math.cos(1)


# In[32]:


dir(math)


# ## 2. 第三方模块
# 
# 安装方法：`pip install [packagename]` 或者`conda install [packagename]`

# In[135]:


from PIL import Image


# In[148]:


import os
os.path


# In[138]:


import tifffile


# In[144]:


tifffile.__path__


# In[139]:


img = tifffile.imread('/Users/sshuair/mindhacks/geopython-tutorial/day2_am/images/RGB.byte.tif')


# In[143]:


tifffile.imshow(img)


# In[43]:


import requests
rsponse = requests.get('http://www.baidu.com')
rsponse.content


# # -----------------面向对象----------------

# ## 1. 定义类

# In[149]:


class Student():
    pass


# In[151]:


# 实例化类
tom = Student()
type(tom)


# ## 2. 类的初始化

# In[152]:


class Student(object):
    def __init__(self, name):
        self.name = name
        
        
tom = Student('tom')
tom.name


# ## 3. 类的方法

# In[153]:


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# In[156]:


jake = Student('jake', 90)
jake.get_grade()


# # -----------------文件读写----------------

# ## 1. 文本文件

# In[166]:


f = open('point.txt', 'r', encoding='utf-8')


# In[162]:


with open('point.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
content[0]


# In[160]:


del content[0]
content


# In[165]:


with open('out_fn.csv', 'w') as f:
    for item in content:
        f.write(item)


# ## 2. 图像文件

# In[168]:


type(img)


# In[167]:


from PIL import Image
img = Image.open('image.jpg')
print(img.size)
img


# In[171]:


import numpy as np
img_array = np.array(img)
img_array.shape


# Q: 图像文件如何保存

# In[170]:


img.save('aaa.jpg')

