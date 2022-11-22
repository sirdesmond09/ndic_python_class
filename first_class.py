

# my_number = 10

# to_string = str(my_number)


# print(type(to_string))

# x = 15
# print(4 * (x**2) + 2*x + 1)

# a= 4
# b = 2
# c = 1

# numerator = -b + ( (b**2) - (4*a*c) )**0.5
# denominator = 2*a

# print(numerator/denominator)

# arr1 = [1,2,3,4,5]
# arr2 = [1,2,3,4,5]

# print(13 in arr2)

#### String concatenation

# first_name = "desmond"
# last_name = "nnebue"

# print(first_name+last_name)


# b = "This is a great school"
# print(b[8:15])

# user_name = input("Name: ")
# user_yob = int(input("Year of Birth: "))

# current_year = 2022

# age = current_year - user_yob


# print(f"Hi, {user_name}.\nYou are {age} years old.")

# fname = input("First Name:\n> ")
# lname = input("Last Name:\n> ")

# username = lname[:3] + fname[-3:]

# print(f"Hi, {fname}.\nThank you for signing up. Your username is {username}")


bottle = "desmond"


###### List


# my_list = [1,2,34,5,667, "Bola", "Maryam", "John"]
# print(my_list)

###Question: Given the ages of students in a class, calculate the:
# 1. Mean
# 2. Median
# 3. Range
# 4. Variance
# 5. Standard Deviation
import statistics #import the statistics module

# ages = input("Enter the ages of students, separate them by comma.\n>") #get the input from the users

# list_of_ages = ages.split(",") #split the string into a list of strings

# # print(list_of_ages)


# int_list_of_ages = list(map(int, list_of_ages)) #use map to convert the strings to integer
# stdev = round(statistics.stdev(int_list_of_ages), 3)

# print(f"The mean is {statistics.mean(int_list_of_ages)}") 
# print(f"The median is {statistics.median(int_list_of_ages)}")
# print(f"The mode is {statistics.mode(int_list_of_ages)}")
# print(f"The standard deviation is {stdev}")



# a = [1,2,34,5,6]
# b=[3,4,6,7,64,9]




# print(list(zip(a,b)))


# if 1 > 10:
#     print("10")
# elif 1<10:
#     if 10 % 2 == 0:
#         print("Even number")
# else:
#     print(50)
    
    

# import random
    
# arr = [1,2,3,4,5,6,7,8,9,0]

# q = ""
# for i in range(6):
#     q+=str(random.choice(arr))
    
# print(q)

# a = 1
# while a <= 10:
#     print(a)
    
#     a+=1

import random

# others = "0" + "".join([str(random.choice(range(10))) for _ in range(9)])

# print(others)


print()
