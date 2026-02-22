#Rule based AI python chatbot


import datetime
import time

name=input("welcome Enter your name : ")
presentHour=datetime.datetime.now().hour


if 5<= presentHour <=12:
    print("Good morning",name)
elif 12<= presentHour <=17:
    print("Good afternoon",name)
elif 17 <= presentHour <=21:
    print("Good evening",name)
else:
    print("Good night",name)

print("Hello!!!, Welcome to your chatbot:)")
print("You can ask me basic question, Type 'byee' to exit from the Bot.")

#chatbot Memory creation [Dictionary of responses]
responses={
    "hello":"Hi, Welcome how can i help you?",
    "how are you": "I am very fine, what about you?",
    "who are you": "I am smart AI chatbot.",
    "motivate me": "Keep going, Every bug makes you a better developer.",
    "happy":"Great to hear that!",
}


#Method?Function to get reswponse of Chatbot

def getResponseBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return"I am not able to tell that yet. I am still in learning mode. I will learn that soon.😊"

#Take user input
while True:
    userInput=input("Please ask your question:")
    if "byee" in userInput.lower():
        print("Byee bot! Have a good day💕.")
        break
    reply=getResponseBot(userInput)
    print("Bot response : ",reply)

    time.sleep(1)