#python推导式，作用是快速的生成一组数据，不建议嵌套使用
#表达式的作用是对返回的元素（步骤二，三）进行表达式的操作
# [表达式 for 变量 in 列表]
# [out_exp_res for out_exp in input_list]
#
# 或者
#
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
# name.upper() 的作用是将每个 name 字符串转换为全大写形式
names = ['alice', 'bob', 'charlie', 'dan', 'edith']
upper_names = [name.upper() for name in names]
print(upper_names)

# ########错误代码########
###那么，我来创建一个例子
# a = set([1, 2, 3, 4, 5])
# b ={a.add for i in a if i % 2 == 0}  错误原因：集合无序性，添加的元素全是集合a原有的，返回的是none
# print(b)
# print(type(b))
#
#
# # 正确写法：直接筛选元素
a = {1, 2, 3, 4, 5}
b = {i for i in a if i % 2 == 0}  # 输出 {2,4}
# print(b)
# print(type(b))
# # # 正确写法：对元素做运算
c = {i*2 for i in b if i > 3}     # 输出 {8,10}
print(c)
print(type(c))
#



