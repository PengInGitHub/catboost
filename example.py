def cash(amount):
    
    try:
        amount = int(amount)
    except TypeError:
        print('invalid value type')
        
    if  amount <= 0:
        print('only positive int allowed!')
        return 0
    
    intervals = [20, 10, 5, 2, 1]
    
    for interval in intervals:
        n_times = 0
        while (amount >= interval):
            amount -= interval
            n_times += 1
        if n_times != 0:
            print(interval, n_times)
        
cash('81')


# Hello World program in Python
    
print "Hello World!\n"


# note
# 在递归函数里面，运用了一部分的数学逻辑在里面，能清晰看见数学等式
# 而非递归实现里面数学逻辑其实是隐藏起来的

def factorial(n):
    # return n*(n-1)!
    # exapmle input: 3, output:3*2*1=6
    
    # non recursive
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

def factorial_re(n):
    # output: always n! = n*(n-1)!
    # recursion
    # input: an int
    # output: an int
    if n == 1:
        return n
    else:
       return n*factorial_re(n-1) 


print(factorial_re(6))



# sum n
# return 1+2+3+....+n

def sum_n(n):
    # loop
    res = 0
    while n > 0:
        res += n
        n = n-1
    return res

print(sum_n(100))

def sum_n_re(n):
    # recursion
    if n == 1:
        return n
    return n + sum_n_re(n-1)

print(sum_n_re(100))


def print_str_rev(string, index):
    
    # base case
    if not string or index>=len(string):
        return
    # recursive func
    print_str_rev(string, index+1)
    print(string[index])
    


def print_str_rev(string, index):
    # base case
    if not string or index >= len(string):
        return
    
    # recursive function
    # trust your buddy
    print_str_rev(string, index+1)
    print(string[index])


a = 'never give up hahaha'
print_str_rev(a, 0)