print("Welcome to my Quiz ! ")

playing = input("Do you want to play ? ")

if playing.lower() != "yes" :
  quit()  #We use quit function to quit the program or we can also use exit() 

print("Good , Let's play !")
score = 0

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply" :
  print('correct !')
  score += 1
else :
  print("Incorrect !")
 
answer = input("What does GUI stands for? ")
if answer.lower() == "graphical user interface" :
  print('correct !')
  score += 1
else :
  print("Incorrect !")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory" :
  print('correct !')
  score += 1
else :
  print("Incorrect !")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit" :
  print('correct !')
  score += 1
else :
  print("Incorrect !")

print(f'''You got {score} correct out of 4 Question. ''')

print("Thanks for playing ")
