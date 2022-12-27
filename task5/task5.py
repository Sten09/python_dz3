#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#Негафибоначчи

#def findFib(index):
#    if index == 1:
#        return 0
#    elif index == 2:
#        return 1
#    return findFib(index-1) + findFib(index-2)
#
#
#n = int(input("numbers of numbers:\n"))
#lst = [findFib(i) for i in range(1, n+2)]
##print(lst)
#lst = lst[::-1] + lst[1:]
#print(lst, '\n')


def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a* (-1) ** i)
        a, b =b, b +a


    return list_nums

print(*neg_fib(int(input())))