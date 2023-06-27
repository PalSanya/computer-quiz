print("Welcome to the quiz")
a=0
play = input("Are you ready to play ")
if play.lower() != "yes":
    quit()
else :
    print("Lets play then !")


ques_1 =input("Who is the father of Computer Science? ---  ")
if ques_1.lower() != "charles babbage":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")


ques_2 =input("When was the first computer invented? ---  ")
if ques_2.lower() != "1822":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")

ques_3 =input("Which part is called the brain of the computer? ---  ")
if ques_3.lower() != "cpu":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")

    
ques_4 =input("What is the decimal equivalent of binary number - 10111? ---  ")
if ques_4.lower() != "23":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")



ques_5 =input("What is the langauge made up of binary-coded instructions? ---  ")
if ques_5.lower() != "machine language":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")



ques_6 =input("First neural network computer was invented in which year  --- ")
if ques_6.lower() != "1958":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")



ques_7 =input("Name the first super-computer of India.  --- ")
if ques_7.lower() != "param 8000":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")



ques_8 =input("Who founded the first computer in India? ---  ")
if ques_8.lower() != "jawahar lal nehru":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")



ques_9 =input("ALU in computer stands for?  --- ")
if ques_9.lower() != "arithmetic logic unit":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")



ques_10 =input("Which computer generation number uses AI? ---  ")
if ques_10.lower() != "5":
    print("Incorrect")
else : 
    a=a+1
    print("Correct")
print("Your score out of 10 is",a)