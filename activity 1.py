from colorama import Fore, Style, init
from textblob import TextBlob
init(autoreset=True)
print(Fore.MAGENTA+"\nI am the Sentiment Spy!")
a=input("What about you? Whats your name?\n My name is ")
while True:
    b=input(Fore.MAGENTA+"Write your sentence: ")
    if b.lower()=='exit':
        print(f"Bye {a}")
        break
    blob=TextBlob(b)
    c=blob.sentiment.polarity
    if c>0:
        print(Fore.GREEN+"The statement is positive")
    elif c<0:
        print(Fore.RED+"The statement is negative")
    else:
        print(Fore.YELLOW+"The statement is neutral")