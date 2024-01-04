## Crust and Size
crust <- c("pan", "crispy thin", "extreme cheese", "extreme cheese and sausage") 
size <- c("small", "medium", "large")
## sum <- sumCrust+sumSize

chatbot <- function() {
    print("Hi! This is Pizza shop. How can I help you?")
    print("Please select pizza crust...")
    print("------------------------------------------------------------")
    print(crust)
    print("------------------------------------------------------------")
    userCrust <- readLines("stdin", n=1)
  
    print("Please select pizza size...")
    print("------------------------------------------------------------")
    print(size)
    print("------------------------------------------------------------")
    userSize <- readLines("stdin", n=1)

    print( paste("Your pizza crust is ", userCrust))
    print( paste("Your pizza size is ", userSize))

    if (userCrust == "pan" | userCrust == "crispy thin") {
      sumCrust <- 100
    } else if (userCrust == "extreme cheese") {
      sumCrust <- 200
    } else if (userCrust == "extreme cheese and sausage") {
      sumCrust <- 300
    } else {
      return("Typing Error")
    }
    if (userSize == "small") {
      sumSize <- 0
    } else if (userSize == "medium") {
      sumSize <- 50
    } else if (userSize == "large") {
      sumSize <- 100
    } else {
      return("Typing Error")
    }
  sum <- sumCrust+sumSize
  print( paste("Total is ", sum, "$"))
  print("Thank you very much!!")
}

chatbot()
