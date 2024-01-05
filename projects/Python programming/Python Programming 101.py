# Python Programming 101
# 1) variables
# 2) data types
# 3) data structures
# 4) function
# 5) control flow

# basic expression / calculation
print(1+1)
print(2*2)
print(10/3)
print(10//3)

## power exponent
print(5**2)
print(pow(3,2))
print(abs(-5))

## compare values
1+1 != 2

## python > R
## deep learning => AI software
## software + API, ML

## 1) variables

my_name = "Kang"
salary_2023 = 50000
_ = "Kang" # Able to use underscore to assign the value

income = 50000
expense = 36000
saving = income - expense
print(saving)

my_name = "john doe"
print(my_name)

## delete variable
del saving

## print string
my_name = "Kang"
age = 23
fav_lang = "R"

## fstring
## string template
f"Hi my name is {my_name} and I'm {age} years old and my favorite language is {fav_lang}."

## traditional way to create template
my_name = "Kang"
"Hi my name is {}". format(my_name)

## string + string
## string *3
text = "blackpink" + " in your area!"
text2 = "blackpink" * 3
len(text)

## 2) data types

## 1. int
## 2. float
## 3. str
## 4. bool: True False // TRUE FALSE in R
## python/r is case sensitive

x = "I\"m learning Python"
print(x, type(x))

## newline character \n
## tab \t character
print("Hello\nWorld!")
print("Hello\tWorld!")

poem = """hello world
I'm learning python
and it's similar to R"""
print(poem)

## convert data type
## int() float() str() bool()
x = "100"
print(x, type(x))
x = int(x)
print(x, type(x))

bool(0)

## get input from user
user_name = input("What's your username: ")
print("Hi! " + user_name)
user_age = input("How old are you? ")
print("Your age: " + user_age) # now user_age type is str
print(int(user_age) *2)

## data type
x = 100
print(x, type(x))

## type hint: just guide the valuable to be what type but what type is assign to it is first priority
age: int = "20"
print(age, type(age))

gpa: float = 3.5
print(gpa, type(float))
print(gpa, type(gpa))

university: str  = "Manchester"
print(university, type(university))

## define a new function
def add_two_num(val1, val2):
    return val1+val2

result = add_two_num(5,10)
print(result)

## default argument
def greeting(name = "kang", food = "KFC"):
    return f"Hello! {name}. I like {food}."
greeting(food = "McDonalds", name = "Lisa")

## function get input from user
def greeting_v2():
    name = input("What's your name?")
    return f"Hello {name}!"
greeting_v2()

## function that return multiple values
def demo():
    name1 = input("Pick a name: ")
    name2 = input("Pick a name: ")
    return (name1, name2, 100) # tupple
demo()

## tuple unpacking
friend1, friend2, _ = demo()
print(friend1, friend2)

## 4)  data structure

## 4.1 list
## 4.2 tuple
## 4.3 dictionary
## 4.4 set

## list => use square bracket [ ... ] and Able to use differnet type of data ex. str and int
shopping_list = ["banana", "egg", "bread", 100]

shopping_list

## method list.append() => add something into list
shopping_list.append("noddle")

shopping_list

shopping_list.append("orange")

shopping_list

## update value5 if we know the index
shopping_list[0] = "grape"

shopping_list

shopping_list.insert(2, "milk")

shopping_list

## count items in list
len(shopping_list)

## function vs. method
## OOP Object Oriented Programming
shopping_list.pop() ## remove the last element

shopping_list

## remove specific item
shopping_list.remove("banana")

shopping_list

## add two lists together
item1 = ["banana",  "grape", "orange"]
item2 = ["milk", "bread"]

full_list = item1 + item2
print(full_list, len(full_list))

full_list.sort(reverse = True) # reverse = True , is sort by z to a

full_list

## highlight how to use list
item1 = ["banana", "orange"]
item2 = item1.copy() ## mutable object

item1[0] = "longan"

print(item1, item2)

## tuple () very similar to list
## tuple is immutable; can't update value in it; ()
## while, list is mutable; can update value in it; []
friends = ("toy", "john", "mary")

friends.index("john")

def hello():
    return 1,2,3,4,5 # tuple

hello()
type(hello())

def hello2():
    return [1,2,3,4,5] # list

hello()
type(hello())

def hello3():
    return {1,2,3,4,5} # set

hello()
type(hello())

list_a = [1,2,3,4,5]
print(type(list_a))


## dictionary {}
## key-value pair ## extract data by key, can't by index
def hi():
    return "hi!"

toy = {
    "fname": "Kasidis",
    "lname": "Satangmongkol",
    "age": 35,
    "movie_lover": True,
    "education": "Master Degree",
    "fav_movies": ["The Dark Knight",
                   "Superman",
                   "Spiderman"],
    "function": hi
}

toy["fav_movies"][1]

toy_func = toy["function"]
toy_func()

## update value in dict
## dict is mutable
toy["fname"] = "John"
toy

## del key
del toy["lname"]
toy

## create key
toy["lname"] = "Doe"
toy

# get method by key if not found the key it will return blank not error
toy.get("fname")

toy["fnameeee"] # if not use .get() then not found the key it will reture error

toy.get("happy world") # not found => reture blank

toy["school"] = "DataRockie"
toy

## tuple list dictionary
## ? mutable -> list, dictionary
## ? immutable -> tuple

## set {unique set} => set will not return duplicate value
fruits = ["apple", "orange", "banana", "banana"]
type(fruits)

uniq_set_fruits = set(fruits)

print(uniq_set_fruits,len(uniq_set_fruits), type(uniq_set_fruits))































