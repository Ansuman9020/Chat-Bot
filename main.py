from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("My Bot")

trainer=ChatterBotCorpusTrainer(bot)
corpus_path = 'C:/Users/star/Desktop/PycharmProjects/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)


trainer.train()
main = Tk()

main.geometry("500x500")

main.title("Chatty")
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio, language='en-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognised")

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=200, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()



textF = Entry(main, font=("Verdana", 13))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 13), command=ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)
def repeatL():
    while True:
        takeQuery()
t=threading.Thread(target=repeatL)
t.start()
mainloop()