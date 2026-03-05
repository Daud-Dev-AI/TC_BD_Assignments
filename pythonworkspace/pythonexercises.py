# Variables and Data Types
print("=======================Variables and Data Types==================================")
print("Question 1.1")
name = "Daud Ahmad"
print(name)

print("\nQuestion 1.2")
a = 5
b = 3
temp = a
a = b
b = temp
print("a:", a)
print("b:", b)

print("\nQuestion 1.3")
float_num = 3.14
int_num = int(float_num)
print(int_num)

print("\nQuestion 1.4")
user = input("Enter any value: ")
if type(user) == str:
    print("The input is a string.")
elif type(user) == int:
    print("The input is an integer.")
elif type(user) == float:
    print("The input is a float.")
else:
    print("The input is of another type.")

print("\nQuestion 1.5")
radius = 4
area = 3.14 * radius ** 2
print("Area of the circle:", area)

# Conditional Statements and Loops
print("\n=======================Conditional Statements and Loops==============================")
print("\nQuestion 2.1")
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\nQuestion 2.2")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("\nQuestion 2.3")
user_num = int(input("Enter a number: "))
if user_num % 3 == 0 and user_num % 5 == 0:
    print("Divisible by both 3 and 5")

print("\nQuestion 2.4")
factorialnumber = int(input("Enter a number: "))
factorial = 1
for i in range(1, factorialnumber + 1):
    factorial *= i
print("Factorial of", factorialnumber, "is", factorial)

print("\nQuestion 2.5")
for i in range(0, 101):
    if i % 7 == 0:
        print(i)

# Functions
print("\n=======================Functions==================================")
print("\nQuestion 3.1")
def square(num):
    return num ** 2
print(square(5))

print("\nQuestion 3.2")
def isprimenum(num):
    if num < 2:
        return "Invalid input: number must be greater than 1"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not a prime number"
    return "Prime number"
print(isprimenum(int(input("Enter a number: "))))

print("\nQuestion 3.3")
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(max_of_three(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))))

print("\nQuestion 3.4")
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
    
print(recursive_factorial(int(input("Enter a number: "))))

print("\nQuestion 3.5")
def vowel_count(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count
print(vowel_count(input("Enter a string: ")))

# Data Collections
print("\n=======================Data Collections==================================")
## Lists
print("\n=======Lists=======")
print("\nQuestion 4.1.1")
my_list = [1, 2, 3, 4, 5]
sum = sum(my_list)
print("Sum of the list:", sum)

print("\nQuestion 4.1.2")
my_list.append(6)
print("Appended list:", my_list)
my_list.remove(2)
print("List after removing 2:", my_list)

print("\nQuestion 4.1.3")
sorted_list = sorted(my_list, reverse=True)
print("Sorted list in descending order:", sorted_list)

print("\nQuestion 4.1.4")
repeated_elem = int(input("Enter a number to check: "))
repeatedcount = my_list.count(repeated_elem)
print(f"The number {repeated_elem} appears {repeatedcount} times in the list.")

print("\nQuestion 4.1.5")
new_list = [2,5,1,2,8,6,32,5]
even_list = []
for i in new_list:
    if i % 2 == 0:
        even_list.append(i)
print("Even numbers in the list:", even_list)

## Tuples
print("\n=======Tuples=======")
print("\nQuestion 4.2.1")
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
print("Second element of the tuple:", my_tuple[1])

print("\nQuestion 4.2.2")
even_tuple = tuple(even_list)
print("Tuple of even numbers:", even_tuple)
print("Printing Type of even_tuple:", type(even_tuple))

print("\nQuestion 4.2.3")
def first_and_last(tup):
    if len(tup) == 0:
        return None
    return (tup[0], tup[-1])
print(first_and_last(my_tuple))

print("\nQuestion 4.2.4")
searchquery = int(input("Enter a number to search in the tuple: "))
if searchquery in even_tuple:
    print(f"The number {searchquery} is present in the tuple.")
else:
    print(f"The number {searchquery} is not present in the tuple.")

print("\nQuestion 4.2.5")
cartuple = ("Volkswagen", "Ford", "Jeep", "Toyota", "Honda")
car1, car2, car3, car4, car5 = cartuple
print("Car 1:", car1, "Car 2:", car2, "Car 3:", car3, "Car 4:", car4, "Car 5:", car5)

## Sets
print("\n=======Sets=======")
print("\nQuestion 4.3.1")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection)

print("\nQuestion 4.3.2")
set1.add(6)
print("Set1 after adding 6:", set1)

print("\nQuestion 4.3.3")
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list with duplicates:", duplicate_list)
unique_set = set(duplicate_list)
print("Set with unique elements:", unique_set)

print("\nQuestion 4.3.4")
superset = {1, 2, 3, 4, 5}
subset1 = {2, 3}
subset2 = {6, 7}
if subset1.issubset(superset):
    print("subset1 is a subset of superset.")
else:
    print("subset1 is not a subset of superset.")

if subset2.issubset(superset):
    print("subset2 is a subset of superset.")
else:
    print("subset2 is not a subset of superset.")

print("\nQuestion 4.3.5")
finalset1 = {5,2,4,2,1,2,8,9,6,3,5,2}
finalset2 = {1,3,5,7,9,11,13,15}
union = finalset1.union(finalset2)
difference = finalset1.difference(finalset2)
print("Union of finalset1 and finalset2:", union)
print("Difference of finalset1 and finalset2:", difference)

## Dictionaries
print("\n=======Dictionaries=======")
print("\nQuestion 4.4.1")
name_and_age = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(name_and_age)

print("\nQuestion 4.4.2")
print(name_and_age.keys())

print("\nQuestion 4.4.3")
name_and_age.update({"David": 28})
print("Updated dictionary:", name_and_age)

print("\nQuestion 4.4.4")
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(char_frequency(input("Enter a string: ")))

print("\nQuestion 4.4.5")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)

# Algorithmic Thinking
print("\n=======================Algorithmic Thinking==================================")
print("\nQuestion 5.1\n")
print("Program to find all prime numbers between 1 and 50")

for num in range(1, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

print("\nQuestion 5.2\n")
print("Reverse a string without using built-in functions")

def reverse_string(s):
    reversed_str = ""
    length = len(s) - 1
    for char in s:
        reversed_str += s[length]
        length -= 1
    return reversed_str

input_string = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(input_string))

print("\nQuestion 5.3\n")
print("find second largest number in a list")

numberlist = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numberlist.sort()
second_largest = numberlist[-2]
print("Second largest number in the list:", second_largest)

print("\nQuestion 5.4\n")
print("Program to count number of words in a string")
input_string = input("Enter a string: ")
word_count = len(input_string.split())
print("Number of words in the string:", word_count)

print("\nQuestion 5.5\n")
print("Program to check if two strings are anagrams")
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print("Anagrams are words or phrases that contain the same letters but in a different order.")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")