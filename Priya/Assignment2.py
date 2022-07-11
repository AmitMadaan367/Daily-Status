#1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# def test_distinct(data):
#       if len(data) == len(set(data)):
#         return True
#       else:
#         return False;
# print(test_distinct([1,5,7,9]))
# print(test_distinct([2,4,5,5,7,9]))

#2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))

#3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
# def remove_nums(int_list):
#   position = 3 - 1                           #(#list starts with 0 index)
#   idx = 0
#   len_list = (len(int_list))
#   while len_list>0:
#     idx = (position+idx)%len_list
#     print(int_list.pop(idx))                  #(Python list pop() is an inbuilt function in Python that removes and returns the last value from the List or the given index value. )
#     len_list -= 1
# nums = [10,20,30,40,50,60,70,80,90]
# remove_nums(nums)

#5. Write a Python program to create the combinations of 3 digit combo
# numbers = []
# for num in range(1000):
#   num=str(num).zfill(3)
# print(num)
# numbers.append(num)

#6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
# string_words = '''India Republic Day is celebrated on 26 January every year. It was 1950 when Dr. Rajendra Prasad our first president hoisted the tricolor on Rajpath, Delhi. Our first chief guest was the President of Indonesia, Mr. Sukarno. Similarly, in 2021 Boris Johnson, Prime Minister of the United Kingdom was invited as a guest of honor but the planning has been recently canceled due to the corona crisis. Every year we invite various famous personalities to be a part of our celebration.

# We have been celebrating this occasion since the year 1950 and it has been declared a national holiday. We celebrate this day because we got our constitution on this day. It took 2 years, 11 months, and 18 days to make our constitution and was completed by 26 November 1949. We also celebrate 26 November as our Constitution day. On 26 January 1950, it was announced to enforce our Constitution for the first time.

# We celebrate this occasion with great enthusiasm and Delhi is the center of the Republic Day celebration. India will celebrate its 73rd Republic Day in the year 2022. The cultural programs will be fewer in number and protocols for COVID-19 will be followed strictly.

# The programme on Rajpath includes a small Parade by various armed forces that will be fewer in number. Children under the age of 15 are strictly prohibited to attend the ceremony. People every year visit Delhi to see this programme but this year only a few spectators are allowed to watch the event to avoid overcrowding amid the pandemic. We can also watch the live telecast of the programme on the national channel Doordarshan.

# Generally, schools also celebrate this occasion and organize various programmes. People all over India celebrate this event by hoisting the flag and distributing sweets. Sometimes they also wear tricolors and play patriotic songs and enjoy their day. This year the republic day celebration will be done in the pandemic situation and therefore the way of celebrating the event is changed. It is necessary to remain safe rather than taking risks.'''
# word_list = string_words.split()

# word_freq = [word_list.count(n) for n in word_list]

# print("String:\n {} \n".format(string_words))
# print("List:\n {} \n".format(str(word_list)))
# print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))

#7. Write a Python program to count the number of each character of a given text of a text file.
# import collections
# import pprint
# file_input = input('File Name: ')
# with open(file_input, 'r') as info:
#   count = collections.Counter(info.read().upper())
#   value = pprint.pformat(count)
# print(value)

# 9. Write a Python program to get a list of locally installed Python modules.
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# for m in installed_packages_list:
#     print(m)


#10. Write a Python program to display some information about the OS where the script is running.
# import platform as pl
# os_profile = [
#         'machine',
#         'node',
#         'platform',
#         'processor',
#         'python_build',
#         'python_compiler',
#         'python_version',
        
#         'system',
#         'uname',
#         'version',
#     ]
# for key in os_profile:
#   if hasattr(pl, key):  
#     print(key +  ": " + str(getattr(pl, key)()))             #(The getattr() function returns the value of the specified attribute from the specified object.)

#14. Write a Python program to add two positive integers without using the '+' operator. Go to the editor
#Note: Use bit wise operations to add two numbers.
# def Add(x, y):
#     while (y != 0):
#         carry = x & y
 
#         x = x ^ y
#         y = carry << 1
#     return x
# print(Add(156, 32))


#15. Write a Python program to check the priority of the four operators (+, -, *, /).
# from collections import deque
# import re
# __operators__ = "+-/*"
# __parenthesis__ = "()"
# __priority__ = {
#     '+': 0,
#     '-': 0,
#     '*': 1,
#     '/': 1,
# }
# def test_higher_priority(operator1, operator2):
#     return __priority__[operator1] >= __priority__[operator2]
# print(test_higher_priority('*','-'))
# print(test_higher_priority('+','-'))
# print(test_higher_priority('+','*'))
# print(test_higher_priority('+','/'))
# print(test_higher_priority('*','/'))

# 16. Write a Python program to get the third side of right angled triangle from two given sides.
# def pythagoras(opposite_side,adjacent_side,hypotenuse):
#         if opposite_side == str("x"):
#             return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
#         elif adjacent_side == str("x"):
#             return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
#         elif hypotenuse == str("x"):
#             return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
#         else:
#             return "You know the answer!"
# print(pythagoras(3,4,'x'))
# print(pythagoras(3,'x',5))
# print(pythagoras('x',4,5))
# print(pythagoras(3,4,5))


# 18. Write a Python program to find the median among three given numbers
# x = input("Input the first number ")
# y = input("Input the second number ")
# z = input("Input the third number ")
# print("Median of the above three numbers -")
# if y < x and x < z:   
#     print(x)
# elif z < x and x < y:
#     print(x)
#     elif z < y and y < x:
#     print(y)
# elif x < y and y < z:
#     print(y)  
# elif y < z and z < x:
#     print(z)    
# elif x < z and z < y:
#     print(z)


