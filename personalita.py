import datetime
from datetime import date

mioNome = "Matte"
assistant = "Robin"

def intro():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        text = "Buongiorno" + mioNome
    elif hour>=12 and hour<18:
        text = "Ciao" + mioNome
    else:
        text = "Buonasera" + mioNome   
    return text 

def orario():
    return "sono le " + str(datetime.datetime.now().hour) + " e " + str(datetime.datetime.now().minute)

def data_oggi():
    today = date.today()
    return "oggi è " + str(today.strftime("%d %B"))

def domande_personali():
    return "sono Robin"