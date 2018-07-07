
"""Write function avg which calculates average of numbers in given list.

Python:

Due to rounding issues please do not use statistics.mean or such.
If the array is empty, return 0"""""

def find_average(array):
    if len(array) > 0:
        return sum(array)/len(array)
    else:
        return 0

"""Is Prime
Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself."""


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

"""Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number."""


def Descending_Order(num):
    if num > 0:
        return int("".join(sorted(str(num), reverse=True)))
    else:
        return 0

"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""

def array_diff(a, b):
    l1 = a
    l2 = b
    l3 = [e for e in l1 if e not in l2]
    return l3

##def array_diff(a, b):
##    return [x for x in a if x not in b]


"""In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

You have to write a function printer_error which given a string will output the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

#Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"""


def printer_error(s):
    a = 0
    for i in range(0,len(s)):
        if s[i] not in 'abcdefghijklm':
            a += 1
    return '{}/{}'.format(str(a),len(s))

#def printer_error(s):
#    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

"""This kata is about multiplying a given number by eight if it is an even number and by nine otherwise."""

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']"""

def solution(s):
    return [s[x:x + 2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

#def solution(s):
#    result = []
 #   if len(s) % 2:
  #      s += '_'
  #  for i in range(0, len(s), 2):
 #       result.append(s[i:i+2])
   # return result

"""Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"""

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))




def race(v1, v2, g):
    h = int(g/(v2-v1))
    m = int((g % (v2-v1)) * 60 / (v2-v1))
    s = int((((g % (v2-v1)) * 60) % (v2-v1)) * 60 / (v2-v1))
    return None if v1 >= v2 else [h, m, s]

#def race(v1, v2, g):
#    if v1>v2: return None
#  res = g*3600/(v2-v1)
#   return [res/3600,res%3600/60,res%60]


"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Uniqu"""

def find_uniq(arr):
        # your code here
        arr.sort()

        if (arr[0] < arr[len(arr) - 1] and arr[0] < arr[len(arr) - 2]):
            n = arr[0]
        else:
            n = arr[len(arr) - 1]

        return n  # n: unique integer in the array

#def find_uniq(arr):
#    a, b = set(arr)
#    return a if arr.count(a) == 1 else b

def century(year):
    # Finish this :)
    return int(year / 100 + 1)

print(century(188))


"""Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

Unfortunately for you, your drive is very bumpy! Given a string showing either flat road ("_") or bumps ("n"), work out if you make it home
 safely. 15 bumps or under, return "Woohoo!", over 15 bumps return "Car Dead"."""

def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"

