
# # # name = "Pat"
# # # age = 22

# # # if not name:
# # #     print("Name is empty")
# # # else:
# # #     print(name)

# # # if age < 18:
# # #     print("Minor")
# # # elif age >= 18:
# # #     print("adult")
# # # else:
# # #     print("???")

# # # message = "Elegible" if age >= 18 else "Not Eligible"
# # # print(message)


# # # arr = ['e', 'r', 'g', 't']
# # # for x in arr:
# # #     i = arr.length

# # # print(x)

# # # names = ["Joe", "pat", "Kim"]
# # # found = False
# # # for name in names:
# # #     if name.startswith("p"):
# # #         print("Found")
# # #         break
# # # else:
# # #     print("Not found")
# # # guess = 0
# # # answer = 5

# # # while answer != guess:
# # #     guess = int(input("Guess: "))


# # # # findTheNthElementFib(8)
# # # def fizzBuzz(num):
# # #     if num % 5 == 0 and num % 3 == 0:
# # #         return "FizzBuzz"
# # #     elif num % 3 == 0:
# # #         return "Fizz"
# # #     elif num % 5 == 0:
# # #         return "Buzz"
# # #     else:
# # #         return num


# # # print(fizzBuzz(7))

# # # # string
# # x = "frog"

# # # print(x[0])
# # # print(x[1:4])

# # x = x + ' prince'

# # # print(' ' in x)
# # # print(max(x))


# # # # list

# # x = ['white', 'pink', 'yellow', 'black', 'blue']
# # print(sorted(x, key=lambda k: k[1]))
# # a, b, c, d, e = x
# # print(b, c, a, e, d)
# # # print(x[-1])
# # # print(x[2:4])
# # # print('pink' not in x)
# # # print(min(x))

# # # # tuple
# # # x = ('Bill', "Pat", 'Paul', 'Tim', 'Kim', 'Bo')

# # # print(x[1])
# # # print(x[:4])
# # # print(x[1:5:2])
# # # print(x[-2])
# # # print(x[:-3])

# # # x = x + ('Mary', 'jane',)
# # # x = x * 3
# # # print('Deb ' not in x)
# # # print(min(x))

# # print(x)
# # x = [1, 2, 3, 4, 5]
# # print(sum(x))
# # print(sum(x[2:4]))
# # print(sum(x[-2:]))
# # print(x.pop())
# # print(x)
# # x.remove(3)
# # print(x)
# # x.reverse()
# # print(x)
# # print('-' * 5)
# # print(sorted(x))
# # print(x)
# # print(x.sort())
# # print(x)
# # print(x.sort(reverse=True))
# # print(x)
# # print(x.count('r'))
# # del(x[0])
# # print(x)
# # x.append(7)
# # # Lists Explained
# # print(x)

# # x = list()
# # y = [1, 'mary', "female", 132.5]
# # tuple1 = (12, 6, 3, 2)
# # z = list(tuple1)
# # y.insert(2, "collins")
# # print(y)
# # a = [m for m in range(100)]
# # print(a)
# # b = [i ** 2 for i in range(10) if i < 4]
# # print(b)
# # a.extend(b)
# # print(a)

# a = ()
# b = 1, 2
# print(a, b, type(a))
# d = [4, 5, 6]
# c = tuple(d)
# e = ([0, 1, 3], 'Abe', 5, 6, 7)

# print(d, type(c))
# del(e[0][1])
# print(e, type(c))
# e += ('Mary',)
# print(e)

# # Sets
# # faster than lists
# # unique items only

# # constructors

# # f = {1, "Angie"}
# # f = {1, "Angie"}
# # g = set()
# # list1 = [2, 3, 4, 5]
# # h = set(list1)
# # i = {1, 1, 1, 1, 1}
# # print(g)
# # print(f)
# # print(h)
# # h.remove(3)
# # print(h)
# # print(i)
# # f.add('2237 main st')
# # print(f)
# # print(len(f))
# # f.add('CA')
# # print(f)
# # print('CA' in f)
# # print(len(f))
# # print(f.pop(), f)
# # f.clear()
# # print(f)

# # # # Mathematical set ops
# # # print("Mathematical set ops")
# # # s1 = {1, 2, 3}
# # # s2 = {3, 4, 5}
# # # print(s1 & s2)
# # # print(s1 | s2)
# # # print(s1 ^ s2)
# # # print(s1 - s2)
# # # print(s2 - s1)
# # # s3 = (s1 | s2)
# # # print(s3 >= s1)-
# # # print(s3 >= s2)

# # # # Dictionaries
# # # They are key value pairs that cannot be sorted
# # # x = {'bedroom1': 128, 'living room': 234, 'kitchen': 176}
# # # print(x)
# # # x['hallway'] = 80
# # # print('#'*10)
# # # print(x)
# # # print(x.keys())
# # # print(x.values())
# # # print(x.items())
# # # print('hallway' in x)
# # # print('kitchen' in x.values())
# # # print('#'*10)


# # # for key in x:
# # #     print(key, x[key])

# # # print('#'*10)
# # # for key, value in x.items():
# # #     print(key, value)

# # # # y = dict([('bedroom1', 128), ('living room', 234), ('kitchen', 176)])
# # # # print(y)
# # # # del(y['kitchen'])
# # # # print(y)

# # # # w = dict(bedroom1=128, livingroom=234, kitchen=176)
# # # # print(w)
# # # # w.clear()
# # # # print(w)6'~^~^^^^^^~~^^^^^^^`````~~~~~~^~^"

# # # List Comprehensions
# 6import random
#
# under_18 = [x for x in range(18)]
# print('under_18: ' + str(under_18))
# squares = [x**2 for x in range(18)]
# print('squares: ' + str(squares))
# odds = [x for x in range(18) if x % 2 == 1]
# print('odds ' + str(odds))
# s = "I love 2 go t0 the store 7 times a w3ek."
# nums = [x for x in s if x.isnumeric()]
# print('nums = ' + " ".join(nums))
#
# names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
# idx = [k for k, v in enumerate(names) if v == 'Anu']
# print('index = ' + str(idx[0]))
# letters = [x for x in 'ABCDEFG']
# random.shuffle(letters)
# letrs = [a for a in letters if a != 'C' and a != 'A']
# print(letters, letrs)
#
# Learning Stacks in Python
# A list is the perfect data structure for a stack
# Use append to push an item onto the stack
# Use pop to remove an item
#
# my_stack = list()
# my_stack.append(1)
# my_stack.append(2)
# my_stack.append(3)
# my_stack.append(4)
# my_stack.append(5)
# my_stack.append(6)
# print(my_stack)
#
# my_stack2 = [x for x in range(7) if x != 0]
# print(my_stack2)
#
# while len(my_stack) > 0:
# if len(my_stack) > 0:
# print(my_stack.pop())
# else:
# print("Done!")
#
# print('my_stack: ', my_stack)
#
#
# class Stack():
# def __init__(self):
# self.stack = list()
#
# def push(self, item):
# self.stack.append(item)
#
# def pop(self):
# if len(self.stack) > 0:
# return self.stack.pop()
# else:
# return None
#
# def peek(self):
# if len(self.stack) > 0:
# return self.stack[len(self.stack)-1]
# else:
# return None
#
# def __str__(self):
# return str(self.stack)
#
#
# Test Code for our Stack wraper
#
# my_stack = Stack()
# my_stack.push('a')
# my_stack.push('b')
# my_stack.push('c')
# my_stack.push('d')
# my_stack.push('e')
# my_stack.push('f')
# print(my_stack)
# print(my_stack.pop())
# print(my_stack.peek())
# print(my_stack.pop())
# print(my_stack)
#

# Implementing Queues in Python
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())


class Queue():
    def __int__(self):
        self.queue = deque()
        self.queue.append(1)

    def addItem(self, item):
        self.queue.append(item)

    def removeItem(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            None

    def peek_front(self):
        if len(self.queue) > 0:
            print(self.queue[len(self.queue)-1])
        else:
            None

    def str(self):
        print(str(self))


# Test Code for Queue
fresh_queue = Queue()
fresh_queue.addItem(1)
print(str(fresh_queue))
# fresh_queue.addItem('a')
# fresh_queue.addItem('b')
# fresh_queue.addItem('c')
# fresh_queue.addItem('d')
# fresh_queue.addItem(1)
# fresh_queue.addItem('blue')
# fresh_queue.addItem('green')
# fresh_queue.addItem(1.5)
# fresh_queue.str()
