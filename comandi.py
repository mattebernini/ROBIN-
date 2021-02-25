import re
import webbrowser
import csv
import wikipedia
import os
import os, shutil
import personalita as AR 

# setup speaker
import pyttsx3
speaker = pyttsx3.init('sapi5') 
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
def speak(text):
    speaker.say(text)
    speaker.runAndWait()

# funzionalità
#*********************************************************
def apri_in_chrome(comando):
    reg_ex = re.search('open google (.*)', comando)
    url = ""
    with open("./memoria/url.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")
        for riga in lettore:
            if riga[0] == comando:
                url = riga[1]
                break

    if url == "":
        return
    print(url)

    if reg_ex:
        subreddit = reg_ex.group(1)
        url = url + 'r/' + subreddit
    webbrowser.open(url)


def wiki():
    wikipedia.set_lang("it")
    speak("cosa vuoi sapere?")
    ricerca = input("...?")
    try:
        risultato = wikipedia.page(ricerca)
        print(risultato.title)
        print(risultato.url)
        speak(wikipedia.summary(ricerca, sentences=2))
        print(risultato.summary)
    except wikipedia.exceptions.DisambiguationError(ricerca):
        speak("cercatelo da solo")
    except  wikipedia.exceptions.PageError:
        speak("stai forse scherzando?")


#***********************************************************
def riceviComando(comando):

    with open("./memoria/url.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")
        for riga in lettore:
            if riga[0] == comando:
                speak("apro" + comando) 
                apri_in_chrome(comando)
                break
    
    if comando == "wikipedia":
        wiki()

    with open("./memoria/path_eseguibili.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")
        for riga in lettore:
            if riga[0] == comando:
                speak("apro" + comando)
                os.startfile(riga[1])
                break 
    
    if comando == "ora":
        speak(AR.orario())
    if comando == "data":
        speak(AR.data_oggi())

    if comando == "ciao":
        speak ("alla prossima!")
    
    

