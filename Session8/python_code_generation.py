# write a python function to return count of number of vowels in a sentence
def count_vowels(sentence):
   count = 0
   for letter in sentence:
      if letter in "aeiouAEIOU":
         count += 1
   return count


# write a python function to check if a given string is a palindrome
def is_palindrome(string):
   return string == string[::-1]


# write a program to print the nth fibonacci number
n1 = 1
n2 = 1
n = 5
for _ in range(n):
   n1, n2 = n2, n1 + n2
print(n2)


# write a function to return the square of first N numbers
def get_squares(n):
   return [i*i for i in range(n)]


# write a python function to return only even numbers in a list
def filter_even(nums):
   return list(filter(lambda num: num % 2 == 0, nums))


# write a python function to return only odd numbers in a list
def filter_odd(nums):
   return list(filter(lambda num: num % 2 == 1, nums))


# write a python program to calculate the sum of numbers using reduce and print it
from functools import reduce
nums = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
total_sum = reduce(lambda a, b: a + b, nums)
print(f'Sum: {total_sum}')


# write a python program to print unique numbers in a list
numbers = [1, 2, 2, 3, 4, 4, 5, 6]
unique = set(numbers)
print(f'Unique numbers: {list(unique)}')


# write a python program to count how many times each letter occurs in a string
string = 'The quick brown fox jumps over the lazy dog'
countmap = {}
for letter in string:
   if letter in countmap:
      countmap[letter] += 1
   else:
      countmap[letter] = 1
print(f'Count of letters: {countmap}')


# write a python function to repeat a given string n times
def repeat_string(string, frequency):
   return string * frequency


# write a program to capitalize the first letter of every word in a string and print it
string = 'The quick brown fox jumps over the lazy dog'
print(string.title())


# write a function that merges two dictionaries
def merge_dictionaries(dict1, dict2):
   return {**dict1, **dict2}


# write a program to merge two lists into a dictionary
keys = [1, 2, 3]
values = ['aye', 'bee', 'sea']
dictionary = dict(zip(keys, values))


# write a python function that inverts the key and values in a dict and returns it
def invert_dict(dictionary):
   inverted_dict = {value: key for key, value in dictionary.items()}
   return inverted_dict


# write a python program to print the difference in days between two dates
from datetime import date
date1 = date(2020, 10, 25)
date2 = date(2020, 12, 25)
print(f'Difference between dates: {(date2 - date1).days}')


# write a python function that returns the weighted average of numbers
def get_weighted_average(numbers, weightage):
   return sum(x * y for x, y in zip(numbers, weightage)) / sum(weightage)


# write a python program to print if year is a leap year or not
year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
      if (year % 400) == 0:
         print("{0} is a leap year".format(year))
      else:
         print("{0} is not a leap year".format(year))
   else:
      print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


# write a python program to check and print if a number is prime
num = 407
if num > 1:
   for i in range(2,num):
      if (num % i) == 0:
         print(num,"is not a prime number")
         break
   else:
      print(num,"is a prime number")
else:
   print(num,"is not a prime number")


# write a python program to print all prime numbers in a given interval
lower = 900
upper = 1000
for num in range(lower, upper + 1):
   if num > 1:
      for i in range(2, num):
         if (num % i) == 0:
               break
      else:
         print(num)


# write a python function to return words in a sentence in sorted order
def get_sorted_words(sentence):
   words = [word for word in sentence.split()]
   words.sort()
   return words


# write a python function to remove all punctuation from a string
def remove_punctuations(sentence):
   punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   no_punct = ''
   for char in sentence:
      if char not in punctuations:
         no_punct = no_punct + char
   return no_punct



# write a python function to return the nth fibonacci number
def fib(n):
   if n <= 1:
      return n
   else:
      return (fib(n-1) + fib(n-2))


# write a python function to return the sum of first n numbers
def sum_of_nums(n):
   if n <= 1:
      return n
   else:
      return n + sum_of_nums(n-1)


# write a python function to return the factorial of a number
def fact(n):
   if n == 1:
      return n
   else:
      return n * fact(n-1)


# write a python program to print the factors of a number
num = 320
for i in range(1, num + 1):
   if num % i == 0:
      print(i)


# write a python function that returns the lcm of two numbers
def lcm(x, y):
   if x > y:
      greater = x
   else:
      greater = y
   
   while(True):
      if((greater % x == 0) and (greater % y == 0)):
         lcm = greater
         break
      greater += 1
   
   return lcm


# write a python function that returns the gcd of two numbers
def gcd(x, y):
   if x > y:
      smaller = y
   else:
      smaller = x

   for i in range(1, smaller + 1):
      if((x % i == 0) and (y % i == 0)):
         gcd = i
   
   return gcd


# write a python program to print the ASCII value of a character
character = 'x'
print(f'The ASCII value of {character} is {ord(character)}')


# write a python program to print the character of an ASCII value
value = 65
print(f'The ASCII value {value} is of the character {chr(value)}')


# write a python function to print the binary value of a decimal number
def print_binary(dec):
   print(bin(dec))


# write a python function to print the octal value of a decimal number
def print_octal(dec):
   print(oct(dec))


# write a python function to print the hexadecimal value of a decimal number
def print_hexadecimal(dec):
   print(hex(dec))


# write a python program that prints the sum of natural numbers up to a given number
num = 16
sum = 0
while (num > 0):
   sum += num
   num -= 1
print(f'The sum is {sum}')


# write a python function to return the number of lines in a file
def count_lines(filename):
   with open(filename, 'r') as f:
      contents = f.read().split('\n')
      return len(contents)


# write a program to print the current date and time
from datetime import datetime
now = datetime.now()
print(now)


# write a python program to extract the file name and extension of a file
import os
filename, extension = os.path.splitext('/path/to/some/file.ext')

# write a python program to merge two lists
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
odd.extend(even)


# write a python program to print a random vowel
import random
vowels = ['a', 'e', 'i', 'o', 'u']
print(random.choice(vowels))


# write a python program to flip a coin 100 times and print number of heads and tails
import random
heads = 0
tails = 0
for i in range(100):
   if(random.choice([True, False])):
      heads += 1
   else:
      tails += 1
print(f'{heads} heads, {tails} tails')


# write a python program to print common elements in two lists
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [2, 4, 6, 8, 10]
print(f'Common elements: { set(list_a).intersection(set(list_b)) }')


# write a python program to print squares of numbers until 20
for i in range(20):
   print(i*i)


# write a python program to print the number of uppercase and lowercase letters in a string
sentence = 'The Quick Brown Fox'
lowercase = 0
uppercase = 0
for c in sentence:
   if c.isupper():
      uppercase += 1
   elif c.islower():
      lowercase += 1
   else:
      pass
print(f'Lowercase: {lowercase}, Uppercase: {uppercase}')


# write a python program to print the number of letters and digits in sentence
sentence = 'The Quick 123 Fox'
digits = 0
letters = 0
for c in sentence:
   if c.isdigit():
      digits += 1
   elif c.isalpha():
      letters += 1
   else:
      pass
print(f'Digits: {digits}, Letters: {letters}')


# write a python function to print a given string n times
def printn(string, n):
   print(string * n)


# write a python program that creates a dictionary whose keys are numbers from 1 to 10 and values are squares of the key
square_dict = {}
for i in range(1, 11):
   square_dict[i] = i*i


# write a python class called Person that has a name property
class Person:
   def __init__(self, name):
      self.name = name


# write a python function that takes two strings as a parameter and prints the shorter one
def print_shorter(str1, str2):
   if (len(str1) > len(str2)):
      print(str2)
   else:
      print(str1)


# write a program to compute the count of each word in a sentence and print it
word_freq = {}
line = 'how many how words does this many have'
for word in line.split():
   word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)


# write a python function that squares every number in a list using a list comprehension and returns the result
def square_numbers(nums):
   return [i*i for i in nums]


# write a python program that converts a binary number to decimal and prints it
binary_num = '1010101'
decimal_num = int(binary_num, 2)
print(decimal_num)


# write a python program that converts a octal number to octal and prints it
octal_num = '17'
decimal_num = int(octal_num, 8)
print(decimal_num)


# write a python program that converts a hexadecimal number to hexadecimal and prints it
hexadecimal_num = 'FF'
decimal_num = int(hexadecimal_num, 16)
print(decimal_num)


# write a python program that alphabetically sorts the words in a sentence and prints it
sentence = 'the quick brown fox jumps'
sorted_words = sentence.split(' ')
sorted_words.sort()
print(' '.join(sorted_words))


# write a python program that prints the area of a circle
import math
radius = 5
print(f'Area: {math.pi * radius * radius}')


# write a python function that returns a dictionary with the area and perimeter of a rectangle
def calculate_rect_properties(width, height):
   return {
      'perimeter': 2 * (width + height),
      'area': width * height
   }


# write a python program that removes all blank spaces in a sentence and prints it
sentence = 'the quick brown fox'
print(sentence.replace(' ', ''))


# write a python program that prints all characters at even indexes in a sentence
sentence = 'the quick brown fox'
print(sentence[::2])


# write a python program that prints every third character in a sentence
sentence = 'the quick brown fox'
print(sentence[::3])


# write a program to remove odd numbers from a list using list comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8]
no_odd_nums = [i for i in nums if i % 2 == 0]


# write a program to remove even numbers from a list using list comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8]
no_even_nums = [i for i in nums if i % 2 == 1]


# write a program to print 5 random numbers between 100 and 200
import random
print(random.sample(range(100, 200), 5))


# write a program to print 5 even random numbers between 10 and 100
import random
print(random.sample([i for i in range(10, 100) if i%2 == 0], 5))


# write a program to print 5 odd random numbers between 100 and 200
import random
print(random.sample([i for i in range(10, 100) if i%2 == 1], 5))


# write a program to print 5 random numbers divisible by 4 between 100 and 200
import random
print(random.sample([i for i in range(10, 100) if i%4 == 0], 5))


# write a program that adds corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
sum_list = [a+b for (a,b) in zip(list1, list2)]
print(sum_list)


# write a program that subtracts corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
diff_list = [a-b for (a,b) in zip(list1, list2)]
print(diff_list)


# write a program that multiplies corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
prod_list = [a*b for (a,b) in zip(list1, list2)]
print(prod_list)


# write a program that divides corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
quot_list = [a/b for (a,b) in zip(list1, list2)]
print(quot_list)


# write a python program to print 5 random vowels
import random
vowels = ['a', 'e', 'i', 'o', 'u']
print([random.choice(vowels) for _ in range(5)])


# write a python program that creates a dictionary whose keys are numbers from 1 to 10 and values are cubes of the key
cube_dict = {}
for i in range(1, 11):
   cube_dict[i] = i ** 3


# write a program to create a string variable and print the amount of memory it consumes
import sys
string_var = 'string variable'
print(sys.getsizeof(string_var))


# write a python function that joins strings in a list and returns the result
def join_string_parts(str_list):
   return " ".join(str_list)


# write a python program that reverses an integer and prints it
num = 12345
reversed = int(str(num)[::-1])
print(reversed)


# write a python program that sorts and prints a comma separated list of values
values = 'one,two,three,four,five'
items = values.split(',')
items.sort()
print(','.join(items))


# write a python program to print unique words in a sentence
sentence = 'the king is the one'
unique = set(sentence.split(' '))
print(unique)


# write a python program that multiplies a tuple n times and print the result
my_tuple = (1, 2, 3)
n = 3
print(my_tuple * 3)


# write a python program to multiply three numbers and print the result
num1 = 2
num2 = 4
num3 = 6
print(num1 * num2 * num3)


# write a python program to print the sum of first n numbers
n = 10
sum = 0
while n > 0:
   sum += n
   n -= 1
print(sum)


# write a python program to print the factorial of a number
num = 5
fact = 1
while num > 0:
   fact *= num
   num -= 1
print(fact)


# write a python function to return the factors of a number
def get_factors(num):
   factors = []
   for i in range(1, num + 1):
      if num % i == 0:
         factors.append(i)
   return factors


# write a python function that returns True if the product of two provided numbers is even
def is_prod_even(num1, num2):
   prod = num1 * num2
   return not prod % 2


# write a python function that returns True if the sum of two provided numbers is even
def is_prod_even(num1, num2):
   sum = num1 + num2
   return not sum % 2


# write a python program to print the first 5 items in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[:5])


# write a python program to print the last 3 items in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[-3:])


# write a python program to print the items in a list apart from the first 4
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[4:])


# write a python function that makes all negative values in a list zero and returns it
def make_negative_zero(items):
   return [0 if item < 0 else item for item in items]


# write a python program to shuffle the items in a list and print it
from random import shuffle
mylist = [1, 2, 3, 4, 5]
shuffle(mylist)
print(mylist)


# write a python program that adds the elements of a list to a set and prints the set
my_set = {1, 2, 3}
my_list = [4, 5, 6]
my_set.update(my_list)
print(my_set)


# write a python program that prints the circumference of a circle
import math
radius = 10
print(f'Area: {2 * math.pi * radius}')


# write a python program that prints the area of a rectangle
length = 10
width = 5
print(f'Area: {length * width}')


# write a python program that prints the area of a square
side = 5
print(f'Area: {side * side}')


# write a python program to create a dictionary with numbers 1 to 5 as keys and the numbers in english as values
number_dict = {
   1: 'one',
   2: 'two',
   3: 'three',
   4: 'four',
   5: 'five'
}


# write a python program to remove words less than a specified length from a sentence
sentence = 'this is my sentence and i will write it my way'
minlength = 3
result = [word for word in sentence.split(' ') if len(word) >= minlength]


# write a python program to keep words less than a specified length in a sentence
sentence = 'this is my sentence and i will write it my way'
maxlength = 3
result = [word for word in sentence.split(' ') if len(word) <= minlength]

#### 93

# write a python function that takes a list as an input and converts all numbers to positive numbers and returns the new list
def make_all_positive(nums):
   return [num if num > 0 else -num for num in nums]


# write a python function that takes a list as an input and converts all numbers to negative numbers and returns the new list
def make_all_negative(nums):
   return [num if num < 0 else -num for num in nums]


# write a python function to return a set of all punctuation used in a string
def get_punctuations(sentence):
   punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   used_punctuation = set()
   for char in sentence:
      if char in punctuations:
         used_punctuation.add(char)
   return used_punctuation


# write a python program to print the words in a sentence in reverse order
sentence = 'the quick brown fox'
words = sentence.split(' ')
words.reverse()
print(' '.join(words))


# write a python program to replace each word in a sentence with the length of the word and print it
sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split(' ')
lengths = [str(len(word)) for word in words]
print(' '.join(lengths))


# write a python program to convert a set to a list
myset = {1, 2, 4, 7}
mylist = list(myset)


# write a python program to convert a list to a dictionary where the key is the index and the value is the item in the list
my_list = [1, 8, 1, 2, 2, 9]
my_dict = {key: value for key, value in enumerate(my_list)}
