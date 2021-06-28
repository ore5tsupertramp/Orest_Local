import csv
from csv import writer
import itertools
import random
# 1. Знайти найменше число в списку
import random

lst = [5, 3, 6, 262, 42, 51, 734, 17, 72, 7]
min_num = lst[0]
for i in lst:
    if i < min_num:
        min_num = i
print('Minimum is: ', min_num)
# 2. Вивести в циклі всі парні числа до 100, крім 6, 8, 86 якщо число 90 зустрінеться в списку то перервати його роботу
lst_2 = [1, 2, 5, 2, 6, 8, 90, 110]
for i in lst_2:
    if i % 2 == 0:
        if i > 100:
            continue
        if i == 6:
            continue
        if i == 8:
            continue
        if i == 88:
            continue
        if i == 90:
            break
    print(i)


# 3. Написати функцію що перевіряє чи є строка правильно записаний номер телефона (+380ХХ-ХХХ-ХХ-ХХ)
def phone(x, y):

    return 'Ukraine code is:' + x + ' entered phone number is:' + y


phone_number_raw = input('enter a phone number:')
phone_number = phone_number_raw[0:6] + '-' + phone_number_raw[6:9] + '-' + phone_number_raw[9:11]+'-' + phone_number_raw[11:]
valid_code = '+380'

if valid_code in phone_number and len(phone_number) == 13:
    print('Correct')
else:
    print('Incorrect: Number should start from country code and has length 13 digits')

print(phone(valid_code, phone_number))
# 4. Скільки існує комбінацій пароля 4 символів, якщо відомо що друга цифра 4, 5 або 7, перша не 0, третя менша 6 а четверта більша 7
a = [1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 7], [0, 1, 2, 3, 4, 5], [8, 9]
print('Amount of possible combinations is: ', len(list(itertools.product(*a))))
# 5. За допомогою filter залишити в списку тільки числа кратні 8
lst_3 = [12, 34, 546, 568, 89, 12, 234, 8, 16, 24]
multiples_8 = list(filter(lambda x: x % 8 == 0, lst_3))
print('numbers multiples of 8 are: ', multiples_8)
# 6. Дано список цілих чисел, порахувати скільки чисел з цього списку мають парну кількість цифр
lst_4 = [12, 3, 456, 13, 123456, 1234, 123, 135]
counter = 0
for i in lst_4:
    i = str(i)
    if len(i) % 2 == 0:
        counter += 1
print('Amount of even number in numbers in list is: ', counter)

# 7. Дано ціле число що містить тільки цифри 9 і 6, використовуючи всього одну заміну цифри в числі знайти максимальне число
numm = 96996
str_num = str(numm)
replaced_num = str_num.replace('6', '9', 1)
int_num = int(replaced_num)
print('The maximum number from', numm, 'using only one replacement is: ', int_num)
# 8. Дано ціле число n, згенерувати список довжиною n, сума елементів якого яких рівна 0.(Числа повинні бути унікальні) ( і не повинні бути послідовними )
n = 4
lst_5 = random.sample(range(-10, 10), k=3)
print('sum of list is: ', sum(lst_5 + [-sum(lst_5)]))

# 9. Дано дві строки, перевірити чи є вони анаграмою. Тобто чи з першої строки можна получить іншу за допомогою перестановок букв
word_1 = input('Enter a first word: ')
word_2 = input('Enter a second word: ')
if sorted(word_1) == sorted(word_2):
    print('Word', word_1, 'with replacement is anagram to word', word_2)
else:
    print('False')
# 10. Є файл з даними учнів у форматі Прізвище;ім’я;зріст Написати функцію що зчитує дані з файлу, функцію що добавляє учня до файлу, функцію що перевіряє чи є валідним формат даних що вводить користувач.
with open('class.csv') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)

with open('class.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    new_surname = input('Enter a surname: ')
    new_name = input('Enter a name: ')
    new_height = input('Enter a height: ')
    csv_writer.writerow([new_surname, new_name, new_height])
