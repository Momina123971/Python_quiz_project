"""A game where a user will attempt few questions and in return it will give his total questions he attempt,
   his percentage and the amount of time he used to answer those question."""



import time
print("Welcome to a quiz game")
marks=0
play=input("Do you want to play a game: ")
start_time=time.time()

if play.lower() !="yes":
    quit()
answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Your answer is correct!.")
    marks+=1
else:
    print("Incorrect answer.") 
answer=input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("Your answer is correct!.")
    marks+=1
else:
    print("Incorrect answer.") 
answer=input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Your answer is correct!.")
    marks+=1
else:
    print("Incorrect answer.") 
answer=input("What does PSU stands for? ")
if answer.lower()=="power supply unit":
    print("Your answer is correct!.")
    marks+=1
else:
    print("Incorrect answer.") 
end_time=time.time()
total_time=round(end_time-start_time,2)    
print("Your got "+ str(marks) + " question correct!.")
print("Your percentage is "+ str(marks/4*100)+ "%")
print("You completed it in",total_time,"seconds")                          