#1

def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)


add(1,2)
subtract(1,2)
multiply(1,2)
divide(1,2)


#2
def area(width, height):
    print(width * height)

area(5,10)


#3
def my_sum_func(numbers_list): 
    sum = 0
    
    for i in numbers_list:
        sum = sum + i
    
    print(sum)

my_sum_func([1,2,3,4,5])

#4
def find_min_max(numbers_list):
    min = numbers_list[0]
    max = numbers_list[0]
    
    for i in numbers_list:
        if min > i:
            min = i
        if max < i:
            max = i
    
    print(min,max)

find_min_max([1,2,3,4,5])


#5

def initial_chars(fullname):
    splited_fullname = fullname.split(" ")
    
    firstname = splited_fullname[0]
    lastname = splited_fullname[1]
    
    result = firstname[0] + "." + lastname[0]
    
    print(result)
   

initial_chars("Irakli Chkhetiani")

#6
def average_arithmetic(number_list):
    jami = sum(number_list)
    result = jami // len(number_list)
    print(result)

average_arithmetic([1,2,3])

#7

def is_palindrom(word):
    reversed_word = ''
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]
    
    print(reversed_word == word)


is_palindrom("irakli")

#8
def remove_spaces(word):
    word_without_space = ''
    
    for char in word:
        if char != " ":
            word_without_space = word_without_space + char
    
    print(word_without_space)

remove_spaces("Irakli Chkhetiani")

#9

def my_replace(word,char1,char2):
    replaced_word = ''
    
    for i in word:
        if i == char1:
            replaced_word = replaced_word + char2 
        else:
            replaced_word = replaced_word + i
    
    print(replaced_word)

my_replace("Irakli Chkhetiani", "a", "k")



#10

def func(number_list):
    sum = 0
    quantity = 0
    
    for num in number_list:
        if num >= 0:
            sum = sum + num
        else:
            quantity = quantity + 1
    
    print(sum,quantity)

func([1,2,3,-1,-2,-3])






