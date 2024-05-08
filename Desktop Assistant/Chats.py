import random

Hello = ('hello', 'hey', 'hi')
reply_Hello = ('Hello Sir' , 'Hello Sir, How are you')

Bye = ('goodbye', 'bye', 'exit', 'sleep')
reply_Bye = ('Goodbye Sir', 'Bye Sir')

ThankYou = ('thank you')
reply_ThankYou = ("You're most welcome, feel free to ask any questions!","You're always Welcome Sir")

HowAreYou = ('how are you')
reply_How = ('I am Fine Sir', 'I am Fine Sir, Thank you')

WhoAreYou = ('who are you')
reply_Who = ('I am a ChatBot, I can help in doing your daily tasks!', 'I am a ChatBot, How can I assist you today?')

def Chats(Text):


    for word in Text.split():

        if word in Hello:

            reply = random.choice(reply_Hello)

            return reply

        elif word in Bye:

            reply = random.choice(reply_Bye)

            return reply
        
        elif word in ThankYou:

            reply = random.choice(reply_ThankYou)

            return reply
        
        elif word in HowAreYou:

            reply = random.choice(reply_How)

            return reply
        
        elif word in WhoAreYou:

            reply = random.choice(reply_Who)

            return reply

        else:

            return ""