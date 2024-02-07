print("welcome to my gamy gi ")

playing=input("Do you want to play?")


if playingyes!="yes":
    quit()


print("Okay ! Let's play :)")
score = 0

answer=input(" What does the term CPU stand for?  ")


if answer=="Central Processing unit ": 
    print("hurray ! you got it ")
    score += 1
else:
    print("incorrect!")

answer=input(" What does the term HDD stand for?  ")


if answer=="Hard drive ": 
    print("hurray ! you got it ")
    score += 1

else:
    print("incorrect!")

    answer=input(" What does the term GPU  stand for?  ")


if answer=="Graphics Processing unit ": 
    print("hurray ! you got it ")
    score += 1
else:
    print("incorrect!")


answer=input(" What does the term SSD stand for?  ")


if answer=="Solid state Drive": 
    print("hurray ! you got it ")
    score += 1

else:
    print("incorrect!")


answer=input(" What does the term ALU  stand for?  ")


if answer=="Arthimetic Logic Unit ": 
    print("hurray ! you got it ")
    score += 1

else:
    print("incorrect!")

print("you got" +str(score)+ "questions correct!")
print("you got" +str((score)/5*100)+ "%.")
