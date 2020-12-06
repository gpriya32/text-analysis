from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from nltk import sent_tokenize
import os

# Create object of ChatBot class
bot = ChatBot('PG')
path="C:/Users/Priyanka/Desktop/ML_DEPL/text-analysis/summary/"
filelist=os.listdir(path)

possibilities=[
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'Thanks received your order id.',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An medicine takes 3-5 Business days to get delivered online.',
'Okay Thanks',
'No Problem! Have a Good Day!'
]

for file in filelist:
    f=open(path+file,'r')
    text=f.read()
    tokens=sent_tokenize(text)
    # print(tokens,"\n")
    possibilities=possibilities+tokens
  

# print(possibilities)

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'PG', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3', 
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
)


trainer = ListTrainer(bot)

trainer.train(possibilities)

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)