# my first R program

print("hello world")
print("oppenheimer is very good movie")

library(dplyr)
mtcars %>%
  select(1:5) %>%
  filter(mpg>30)

#first
mtcars %>%
  select(mpg) %>%
  filter(mpg < 30)

#second
mtcars %>%
  select(mpg) %>%
  filter(mpg < 30)
