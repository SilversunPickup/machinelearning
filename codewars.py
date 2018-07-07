
"""Write function avg which calculates average of numbers in given list.

Python:

Due to rounding issues please do not use statistics.mean or such.
If the array is empty, return 0"""""

def find_average(array):
    if len(array) > 0:
        return sum(array)/len(array)
    else:
        return 0





