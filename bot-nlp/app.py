from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from nltk import sent_tokenize
import os

app = Flask(__name__)

# path="C:/Users/Priyanka/Desktop/ML_DEPL/text-analysis/summary/"
# filelist=os.listdir(path)

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
'No Problem! Have a Good Day!',
"#coronavirus", "#COVID19", "#CoronavirusOutbreak", "greetings", "sup", "what's up","hey", "hi Babe", "how are you?",
]

w=open("wiki.txt",'r',encoding='utf-8')
w_text=w.read()
wiki_tokens=sent_tokenize(w_text)
possibilities+=wiki_tokens

# for file in filelist:
#     f=open(path+file,'r')
#     text=f.read()
#     tokens=sent_tokenize(text)
#     # print(tokens,"\n")
#     possibilities=possibilities+tokens

# naming chatbot
bot=ChatBot('PG')

# connecting to sqlite database
bot = ChatBot(
    'PG', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3', 
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch']
)

# traning the bot  and storing result in database
trainer2 = ListTrainer(bot)
trainer2.train(possibilities)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()