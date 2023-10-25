# load ggplot library
# update this file, just another comment


library(ggplot2)

# first plot
ggplot(diamonds, aes(carat, price)) +
  geom_point()

# second plot
ggplot(diamonds, aes(carat, price)) +
  geom_point() +
  geom_smooth()
