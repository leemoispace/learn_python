#fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了
def fact(n):
    if n==1:
        return 1
    return n* fact(n - 1)



#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的
#尾递归是指，在函数返回的时候，调用自身本身
#主要是要把每一步的乘积num * product传入到递归函数中
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


    # 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)# 子目标1
        move(1, a, b, c)# 子目标2
        move(n-1, b, a, c)# 子目标3
n = input('enter the number:')
move(int(n), 'A', 'B', 'C')