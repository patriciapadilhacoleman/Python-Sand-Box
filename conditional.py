# def fizz_buzz(intput):
#     if input % 3 == 0:
#         result = "Fizz"
#     if input % 5 == 0:
#         result = "Buzz"
#     else:
#         print(result)


# fizz_buzz(15)

from collections import Counter

list1 = ['a', "b", 'c', 'c', 'd','a', 'a']
hash = Counter(list1)

for i in hash:
    print(i,str(i.count))
    