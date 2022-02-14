print("Welcome to the Quiz game... ")
print("To start the game press. YEs","\n To Quit game press .No") 

a = input("Entre the key ").lower()
if a!="yes":
    quit()
print("Let's Start game")

score = 0
answer=input("who is the PM of India? ").lower()
if answer=="narendra modi":
    print("correct")
    score+=1
else:
    print("Incorrect")

answer=input("What is the capital of india? ").lower()
if answer=="delhi":
    print("correct")
    score+=1
else:
    print("Incorrect")    

answer=input("who is the father of nation? ").lower()
if answer=="mahatma gandhi":
    print("correct")
    score+=1
else:
    print("Incorrect")
    
answer=input("who is the father of computer? ").lower()
if answer=="charles babbage":
    print("correct")
    score+=1
else:
    print("Incorrect")

answer=input("silicon valley in india? ").lower()
if answer=="bangalore":
    print("correct")
    score+=1
else:
    print("Incorrect")

answer=input("where is taj mahal located in india? ").lower()
if answer=="agra":
    print("correct")
    score+=1
else:
    print("Incorrect")

answer=input("what is india's smallest state ? ").lower()
if answer=="goa":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer=input("what is the Fullform of DSA ? ").lower()
if answer=="direct selling agent":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer=input("FUllform of SRk ? ").lower()
if answer=="Shahrukh Khan":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer=input(" fullform of NEWS? ").lower()
if answer==" Nature Environment and Wildlife Society":
    print("correct")
    score+=1
else:
    print("Incorrect")
print("you scored "+str(score)+" in quiz")
print("your percentage is "+   str((score/10)* 100)  + "%")
    
