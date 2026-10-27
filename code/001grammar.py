#a=input('请输入:')
#print(f'hello{a}')
#print('你好\n世界')
#print('你好世界',end='')
#a=2
#a=a**10
#print(a)#数字变量输出不加引号
# a=False
# b= not a
# c=a or b
# d=a and c
# print(a,b,c,d)
'''s1='o'
s2='h'
s3=s2*2
print(s3)'''
'''a=11
b=a%2
c=b==0
if c:
    print("是偶数")
else:
    print('是奇数')
print('end')'''
'''a=int(input('请输入成绩：'))
if a<0 or a>100:
    print('成绩不合法')
elif a<60:
    print('不合格')
elif a<=80:
    print('合格')
else: #else后面不需要加条件
    print('优秀')'''
'''a=0
while a<10:
    a+=1
    print(a)
else:
    print('end')'''
'''for i in range(10):
    print(i)
    if i==5:
        continue
else:
    print('循环结束')'''
#a="My name is xxx"
#a=a[-5:-1] 输出s xx
#a=a.replace('xxx','pig')#my name is pig
#arr=a.split(' ')#['my', 'name', 'is', 'xxx']
#b=list(a)
#s='-'.join(arr)#my-name-is-xxx
#print(arr)

#print(b)
# b=a.strip()
# print(b)
'''array = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[3, 2, 5], [4, 5, 8], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 8], [7, 0, 9]]
]

for a in array:
    for b in a:
        for c in b:
            print(c)'''
#b=12
#a=[0,False,b,'happy',[1,2,3]]
#if True in a:
#    print('...')
#a[0]=123
#print(a)
#string='avc'
#string[0]='b'字符串是不可变数据类型不能这么写
#print(string)
#a=[4,7,2,6]
#a.sort()
#b=sorted(a)
#print(a)
#列表可以存储任意类型元素，字符串不能直接进行修改（可以
# 转为列表然后修改）
# a=(1,2)#数据结构为元组，不可变，有序，允许重复
# print(a[0])
# s={1,3,3,4}#集合，无序性，不可重复
# print(s)#输出{1, 3, 4}
#d={'name':'pig','age':20}
#a=list(d.items())#/d.keys()/d.values()
#print(a)
#print(a[0])
#for k,v in d.items():
 #   print(k)
  #  print(v)
#a{}表示空字典b=set()表示空集合
# 字典定义，大括号{}，键值对 key:value
'''d = {"name": "Pig", "age": 20}

# 通过键key取值
print(d["name"])

# 修改指定key对应的值
d["name"] = "Fog"

# 删除字典里指定的键值对
del d["age"]

# 清空字典所有元素，字典对象还在，变成空字典
d.clear()

# 删除整个字典对象，变量d直接被销毁
del d'''
'''def g():
    return 1,2
a,b=g()
print(a)
print(b)'''
def f(n,*a):
    print(n)
    for i in a:
        print(i)
f(3,*(1,2,3,4))

