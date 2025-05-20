class FibonacciIterator:
    """斐波那契数列迭代器，生成无限长的斐波那契数列"""
    
    def __init__(self, max_value=None):
        # 初始化方法，设置斐波那契数列的起始值和最大值限制
        self.a, self.b = 0, 1  # a保存当前值，b保存下一个值
        self.max_value = max_value  # 可选的最大值限制

    def __iter__(self):
        # 返回迭代器对象本身
        return self

    def __next__(self):
        # 获取下一个斐波那契数
        if self.max_value is not None and self.a > self.max_value:
            # 如果达到最大值限制，抛出StopIteration异常结束迭代
            raise StopIteration
        value = self.a  # 保存当前值
        self.a, self.b = self.b, self.a + self.b  # 更新斐波那契数
        return value  # 返回当前斐波那契数

# 使用迭代器
if __name__ == "__main__":
    # 创建迭代器实例（限制最大值为100）
    fib_iter = FibonacciIterator(max_value=100)
    
    print("生成的斐波那契数列（最大值不超过100）：")
    for num in fib_iter:
        # 使用迭代器生成并打印斐波那契数列
        print(num, end=' ')  # 打印数字，用空格分隔