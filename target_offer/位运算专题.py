def number0f1(n):
    count = 0
    if n < 0:  ## python的取补码操作比较特殊
        n = n & 0xffffffff
        bin_ = bin(n)
    while n:
        count += 1
        n = (n - 1) & n
    return count
print(number0f1(-3))
