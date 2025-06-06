#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_str):
    # Returns the first five characters of the string
    return input_str[:5]

def last_seven(input_str):
    # Returns the last seven characters of the string
    return input_str[-7:]

def middle_number(num):
    # Converts the number to a string and returns the second and third characters
    num_str = str(num)
    return num_str[1:3]

def first_three_last_three(s1, s2):
    # Returns a string made from the first 3 of s1 and last 3 of s2
    return s1[:3] + s2[-3:]


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
