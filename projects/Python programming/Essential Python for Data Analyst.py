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

## OOP => Object Oriented Programming
## Dog
class Dog:
    # initialize
    def __init__(self, name, age, breed): # __ = dunder (double underscoll)
        self.name = name
        self.age = age
        self.breed = breed

    ## dog methods (functions)
    def sit(self):
        print("I'm  sitting now.")

    def sleep(self):
        print("I'm sleeping now.")

    def get_older(self, year):
        self.age += year

dog1 = Dog("milo", 3, "chihuahua")

dog1.get_older(3)
print(dog1.age)

text = "a duck walks into a bar"

## string method
text.split(" ")

"HELLO WORLD".lower()

## list method
emp_list = []
emp_list.append("apple")
emp_list.append("banana")

emp_list

class Apple:
    def __init__(self, size, price, color):
        self.size = size
        self.price = price
        self.color = color

apple1 = Apple("medium", 5, "red")

print(apple1.size, apple1.price, apple1.color)

## Python Class => OOP
## Class => attribute: name, age, breed
## Class => method: function => sit, sleep, get older

class Person:
    def __init__(self, name):
        self.name = name

## Superclass
class Employee(Person):
    def __init__(self, name, company, position):
        super().__init__(name)
        self.name = name
        self.company = company
        self.position = position
    def greeting(self):
        print(f"Hi my name is {self.name} and I work for {self.company}")

ps1 = Person("kang")
ps2 = Employee("john", "Google", "Data Analyst")

ps1

ps2

ps2.greeting()

ps1.greeting()

## Superclass extend feature from base class => HW02 - class ATM at least 5 methods

## try except block (traping the error with except)
try:
    print(dfgsdfgsdfg)
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Variable not found in our environment")
else:
    print("OK")
finally:
    print("End!")

## try except for syntax error
try:
    eval('print(1+5 ')
except:
    print("Syntax error")

!pwd # Print Working Directory

!ls # list all file in Working Directory

!echo hello world # like print("Hello world")

!cat friends.csv # Concatenate => review data in file ..

import csv

# open csv file using read mode ("r")
file = open("friends.csv", "r")

# read content in this file
data = csv.reader(file)

data

for row in data:
    print(row)

# close file
file.close()

# pandas
import pandas as pd
df = pd.read_csv("friends.csv")

# import csv
df = pd.read_csv("friends.csv")

# export csv
df.to_csv("haha.csv")

df

!cat haha.csv

## context manager => with ; open and close file for user automatically
        # sometime if user forget to close the file after open and get data, the file will broken
## use to open data file

# import csv
from csv import reader
result = []

with open("friends.csv", "r") as file:
    data = reader(file)
    for row in data:
        result.append(row)

result

print(type(result))

## write mode
import csv

header = ["id", "course", "students"]
body_data = [
    [1, "data science", 30],
    [2, "marketing", 28],
    [3, "power BI", 35]
]

with open("courses.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(body_data)

!ls

!cat courses.csv

!cat customer.json

import json
with open("customer.json", "r") as file:
    customer = json.load(file)
print(customer, type(customer))

## dict => json
import json #.load() , .dump()
book = {
    "name": "How to be better at almost everything",
    "year": 2018,
    "author": "Pat Flynn",
    "favorite": True
}

with open("book.json", "w") as file:
    json.dump(book, file)
    print("Create file successfully!")

!cat book.json

import json
with open("book.json", "r") as file:
    book = json.load(file)
print(book, type(book))

!cat courses.csv

try:
    with open("COURSES.csv", "r") as file:
        data = csv.reader(file)
        for row in data:
         print(row)
except FileNotFoundError:
    print("Please check file name again.")
else:
    print("Open file successfully.")

# API => Application Programming Interface
# Communication two machines

# request-reponse cycle
from requests import get

url = "https://swapi.dev/api/people/1"

resp = get(url)

## if success, OK 200
resp.status_code

## see information
resp.json()["name"]

resp.json()

import requests
import time

characters = []

for i in range(5):
    url = f"https://swapi.dev/api/people/{i+1}"
    resp = requests.get(url)
    if resp.status_code == 200:
        json_data = resp.json()
        characters.append(
            (json_data["name"],
            json_data["height"])
        )
    else:
        characters.append("error")

    # break a second
    time.sleep(1)

print(characters)

import requests
import time

characters = []
total_characters = 5  # Assuming there are 10 characters in the SWAPI

for i in range(1, total_characters + 1):
    url = f"https://swapi.dev/api/people/{i}"
    resp = requests.get(url)

    if resp.status_code == 200:
        json_data = resp.json()
        characters.append(
            (json_data["name"], json_data["height"])
        )
    else:
        characters.append("error")

    # break for a second
    time.sleep(1)

print(characters)

url = f"https://swapi.dev/api/people/{i+1}"
print(url)

# web scraping
# install new library on google colab
# pip => package manager in Python

!pip install gazpacho
!pip list | grep "gaz"

## import function
from gazpacho import Soup
import requests

## web scraping basics (ดึงข้อมูลจากหน้าเว็บ)

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

html = requests.get(url, headers=headers) ## Accept-Language: en

html

imdb = Soup(html.text)

titles = imdb.find("h3", {"class": "lister-item-header"})

titles = imdb.find("h3", {"class": "lister-item-header"})

#clean_titles = []

#for title in titles:
#    clean_titles.append(title.strip())

## list comprehension

clean_titles =  [title.strip() for title in titles]

titles[0].strip() # .strip will keep only text element (delete html element)

clean_titles

 ## get rating from the website
 ## div: ratings-imdb-rating

ratings = imdb.find("div", {"class": "ratings-imdb-rating"})

clean_ratings = [float(rating.strip()) for rating in ratings]

clean_ratings

import pandas as pd

# create dataframe
movie_database = pd.DataFrame(data = {
    "title": clean_titles,
    "rating": clean_ratings
})

# print first five rows
movie_database.head()


## Intro to Data Science Libraries
# numpy
# pandas
# sklearn (machine learning)
# statsmodel (statistics)

# numerical python
# very fast
import numpy as np
nums = [1,2,3,4,5]
[num*2 for num in nums] # => [2, 4, 6, 8, 10]
nums = np.array(nums)
type(nums) # => numpy.ndarray
nums /5 # => array([0.2, 0.4, 0.6, 0.8, 1. ])

# STATISTICS CALCULATION
np.median(nums) # => 3.0
nums.sum() # => 15
np.sum(nums) # => 15
np.arange(10)  # range => array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(10) +1 # => array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
np.linspace(0, 10, num=20) # =>     # array([ 0.        ,  0.52631579,  1.05263158,  1.57894737,  2.10526316,
                                    # 2.63157895,  3.15789474,  3.68421053,  4.21052632,  4.73684211,
                                    # 5.26315789,  5.78947368,  6.31578947,  6.84210526,  7.36842105,
                                    # 7.89473684,  8.42105263,  8.94736842,  9.47368421, 10.        ])
## 2D array
n2 = np.array([
    [1,2],
    [3,4]
])
print(n2, type(n2))  # =>   [[1 2]
                     #      [3 4]] <class 'numpy.ndarray'>

## matrix * matrix
## .dot notation
m1 = np.array([[1,2],[5,5]])
m2 = np.array([[4,2],[1,2]])
np.dot(m1,m2) # => array([[ 6,  6],
               #        [25, 20]])

# import pandas
# manage dataframe
import pandas as pd

# read data from csv file
url = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
mtcars = pd.read_csv(url)
type(mtcars) #=> pandas.core.frame.DataFrame
mtcars.shape #=> (32, 12)
mtcars.info()
mtcars.head()
df = mtcars[ ["mpg", "model", "hp"] ].tail(3)
df
df["mpg_double"] = df["mpg"] * 2
df
df["mpg"].mean()
np.mean(df["mpg"])
df["mpg"].mean()

colnames = list(df.columns)
colnames[0] = "New Model"
print(colnames)
df.columns = colnames

df.head()

mtcars["mpg"] > 30

# filter traditional
mtcars[ (mtcars["mpg"] > 30) & (mtcars["hp"] > 100)]

# pandas .query()
# condition used to filter dataframe
mtcars.query(" mpg > 30 and hp > 100 ")

# aggregate + group by
# read data

import pandas as pd
store = pd.read_csv("store.csv")

col_names = list(store.columns)
col_names

clean_col_names = [col.lower().replace(" ", "_").replace("-", "_") for col in col_names]
# clean column names
store.columns = clean_col_names

store.columns

store

store["sales"].sum()

result = store.groupby(["segment","category"])["sales"].sum().reset_index()

# aggregate
store.groupby("segment")["sales"].\ # backslash is for new row.
    agg(["sum", "mean", "std"]).\
    reset_index()

## R version
## store %>% groupby(segment) %>% summarise(sum(sales))

result.to_csv("agg_data.csv")

## read data from sql database
## chinook.db

import sqlite3
import pandas as pd

## create connection
con = sqlite3.connect("chinook.db")

df = pd.read_sql("SELECT * FROM customers WHERE country = 'USA'", con)

## close connect
con.close()

df.head()

df[ df.State == "WA" ]

df[ df["State"] == "WA" ]

import pandas as pd
# sklearn basics
# ref:

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# read data
mtcars = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
mtcars.head()

# prepare data
X = mtcars.drop(["model", "mpg"], axis=1) # axis=1 is column , axis=0 is row
y = mtcars["mpg"]

# split data
# set.seed(42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# train model
model = BaggingRegressor()
model.fit(X_train, y_train)

# prediction
p = model.predict(X_test)

# R squared
model.score(X_test, y_test)

# MAE mean absolute error
# mean(abs(y_test - p))
np.mean(np.abs(y_test - p))

# MSE mean square error
np.mean((y_test - p)**2)

# save model
import pickle

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)




