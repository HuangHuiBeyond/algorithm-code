## 输入：'I love    Guangzhou'
## 输出：'Guangzhou    love I'
## 空格的特定：一组空格翻转之后还是一组空格

def reverse_string(s):
    if not s:
        return ''
    str_list = list(s)
    i = 0
    size = len(str_list)
    
    def reverse(str_list, start, end):
        while start < end:
            str_list[start], str_list[end] = str_list[end], str_list[start]
            start += 1
            end -= 1
    while i < size:
        start = i
        end = i + 1
        if str_list[start] != ' ':
            while end < size and str_list[end] != ' ':
                end += 1
            reverse(str_list, start, end - 1)
            i = end
        else:
            i += 1
    reverse(str_list, 0, size - 1) ## 没有调库，空间复杂度为O（1）
    return str_list
s = 'I love    Guangzhou'
res = reverse_string(s)
print(''.join(res))
    
