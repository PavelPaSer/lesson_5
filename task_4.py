# 3.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

s = input("Введите текст для кодировки: ") 

def coding(t):
    count = 1
    res = ''
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            count += 1
        else:
            res = res + str(count) + t[i]
            count = 1
    if count > 1 or (t[len(t)-2] != t[-1]):
        res = res + str(count) + t[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res



print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")