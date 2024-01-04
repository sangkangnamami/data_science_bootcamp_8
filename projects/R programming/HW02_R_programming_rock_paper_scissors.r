##Pao Ying Choop game
sample_space <- c("rock", "paper", "scissors", "exit")
print("This is rock/paper/scissors game")
print("Please select one.. or exit")
print(sample_space)

##user
user_score = 0
user_input = "0"

##pc
pc_score = 0

play_game <- function() {
while(TRUE) {
  pc_draw <- sample_space[sample(1:3, 1)]
  user_input <- readLines("stdin", n=1)
  print( paste(("PC = "), pc_draw))
  print( paste(("You = "), user_input))
      if (user_input == "rock" & pc_draw == "rock") {
        print("draw")
    } else if (user_input == "rock" & pc_draw == "paper") {
        print("you lose")
        pc_score = pc_score+1
    } else if (user_input == "rock" & pc_draw == "scissors") {
        print("you win")
        user_score = user_score+1
    } else if (user_input == "paper" & pc_draw == "rock") {
        print("you win")
        user_score = user_score+1
    } else if (user_input == "paper" & pc_draw == "paper") {
        print("draw")
    } else if (user_input == "paper" & pc_draw == "scissors") {
        print("you lose")
        pc_score = pc_score+1
    } else if (user_input == "scissors" & pc_draw == "rock") {
        print("you lose")
        pc_score = pc_score+1
    } else if (user_input == "scissors" & pc_draw == "paper") {
        print("you win")
        user_score = user_score+1
    } else if (user_input == "scissors" & pc_draw == "scissors") {
        print("draw")
    } else if (user_input == "exit") {
        break
    } else {
        return("Typing Error")
        break
    }
  }
  print("**************** SUM SCORE ****************")
  print( paste("PC got score = ", pc_score))
  print( paste("You got score = ", user_score))
  print("**************** SUMMARY ****************")
    if (user_score == pc_score) {
      print("You draw")
    } else  if (user_score > pc_score) {
      print(paste("You win with score ", user_score))
    } else {
      print(paste("You lose, PC got score ", pc_score))
    }
}

play_game()
