#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.
#
#in
#88
#out
#1011000

#s = ""
#n = int(input(
#    "Введите число для преобразовывания десятичного числа в двоичное:\n"))
#while n != 0:
#    s = str(n % 2) + s
#    n //= 2
#print(s)

def conv_bin(num: int):
    list_nims = []

    while num > 0:
        list_nims.insert(0, num % 2)
        num //= 2

    print(*list_nims, sep='')

conv_bin(int(input()))