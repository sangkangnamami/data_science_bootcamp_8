## R programming concepts
## 1. variable
## 2. data type
## 3. data structures
## 4. control flow
## 5. function

print("hello world")
print("I am learning R language!")

## 1. create variables
my_name <- "Toy"
age <- 34
fav_language <- "R language"
movie_lover <- TRUE

my_name <- "Kasidis"

## find saving
income <- 50000
expense <- 32000
saving <- income - expense

## 2. data types
## numeric
## character (string, text)
## logical (boolean)
## date

x <- 100
class(x)

my_name <- "toy"
class(my_name)

movie_lover <- FALSE
class(movie_lover)

d <- as.Date("2023-06-10")
class(d)

## 3. data structures
## vector
## matrix
## list
## dataframe

## let's learn vector
1:10
1:25
5:100

seq(1, 30, 2)
rep("toy", 10)

length(score); length(friends)

## data frame

id <- 1:5
friends <- c("toy", "kevin", "mary",
             "anna", "lisa")
age <- c(34, 32, 28, 25, 29)
movie_lover <- c(T, F, F, T, T)

## list
customer01 <- list(
  name = "toy",
  age = 34,
  city = "BKK"
)

customer02 <- list(
  name = "mary",
  age = 28,
  city = "LON",
  email = "mary@google.com"
)

customer03 <- list(
  name = "kevin",
  age = 26,
  city = "JAP",
  address = "Mount Fuji."
)

## NO-SQL document database (JSON)
all_customers <- list(
  toy = customer01, 
  mary = customer02, 
  kevin = customer03
)

## user defined function 

add_two_nums <- function(a, b) a+b

greeting <- function() print("hi!")

greeting_name <- function() {
  name <- readline("What's your name? ")
  print( paste("Hello!", name))
}

double_value <- function() {
  value <- as.numeric(readline("Give me a value: "))
  value * 2
}


## default argument
greeting <- function(name="Toy") {
  print(paste("Hello!", name))
}

## more than one default arguments
check_weather <- function(temp=35, day="Monday") {
  text <- paste("Today:", day, "; temperature:", temp)
  return(text)
}

## control flow
## if, for, while

grading <- function(score) {
  if (score >= 80) {
    return("A")
  } else if (score >= 70) {
    return("B")
  } else if (score >= 60) {
    return("C")
  } else if (score >= 50) {
    return("D")
  } else {
    return("Failed")
  }
}

## two conditions
## [1] weekday vs. weekend
## [2] morning vs. dinner

hotel_menu <- function(day, time) {
  if (day=="weekday" & time=="morning") {
    return("cereal")
  } else if (day=="weekday" & time=="dinner") {
    return("salad")
  } else {
    return("anything you want to eat!")
  }
}

# for loop

fruits <- c("apple", "mango", 
            "orange", "durian", "grape")


for (fruit in fruits) {
  if (fruit == "orange") {
    print("Found Orange!")
  } else {
    print("Other fruits!")
  }
}

# while loop
count <- 0

while (count < 10) {
  print("hello world")
  ## counter
  count <- count + 1
}

chatbot <- function() {
  while(TRUE) {
    user_fruit = readline("Guess the fruit: ")
      if (user_fruit == "mango") {
        print("Correct!")
        break
      } else {
        print("Nope! Try again.")
      }
    }
  }


## HW01 - chatbot order pizza
## chatbot() 

## HW02 - pao ying chub
## play_game()
















