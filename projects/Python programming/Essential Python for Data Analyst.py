## Essential Python for Data Analyst
# control flow + function
# OOP: Object Oriented Programming
# try except handle error
# context manager, csv, json
# API
# web scraping => static website is better
# intro to data science libraries

## function def
def hello(name):
    print("Hi " + name)

# lambda function => use to define function in one line
hello = lambda name: print("Hi " + name)

hello("John")

# control flow
# if/for/while

# if elif else
def grading(score):
    # docstring
    """
    this function return grade for a student in UK
    """
    if score >= 70:
        return "Distinction"
    elif score >= 60:
        return "Merit"
    elif score >= 50:
        return "Passed"
    else:
        return "Failed"
      
grading(44)

# return value from a function
def add_two_num(x,y):
    return x + y

result = add_two_num(10,15)
print(result)

# for loop
nums = [1,2,3,4,5] ## => [2,4,6,8,10]

new_nums = [] # empty list

for num in nums:
    new_nums.append(num*2)

print(new_nums) # => [2, 4, 6, 8, 10]

# list comprehension => shorten the above code
nums = [1,2,3,4,5]
y = [num*2 for num in nums]

print(y)

## program to check odd/ even numbers
nums = [35, 50, 22, 21, 28]
for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# while loop
count = 0
while count < 5: ## True
    print("hello")
    count += 1 # this line is very important

# get input from a user
# animal guessing game
def animal_guessing():
    set_animal = "hippo"
    answers = [] # empty list
    while True:
        guess = input("Guess the animal: ")
        answers.append(guess)
        if guess == set_animal:
            print("Hooray! correct answer")
            print(f"Logs: {answers}")
            break
        elif guess == "quit":
            print("See you next time.")
            break
        else:
            print("Nope! please try again.")
          
animal_guessing()

























