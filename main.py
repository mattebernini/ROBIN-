import speech_recognition as sr 
import personalita  
import spartitraffico  
import comandi

# setup Riconoscitore
riconoscitore = sr.Recognizer()

def ascolta():
    with sr.Microphone() as source:
        print("...")
        riconoscitore.pause_threshold = 1
        audio = riconoscitore.listen(source)
        riconoscitore.adjust_for_ambient_noise(source)
    try:
        query = riconoscitore.recognize_google(audio, language="it-IT")
        print("ho capito: \n", query)
    except Exception as e:
        return "None"
    return query 



if __name__ == "__main__":
    comandi.speak(personalita.intro())

    while True:

        domanda = ascolta().lower()
        comando = spartitraffico.scegli(domanda)

        comandi.riceviComando(comando)

        if comando == "ciao":
            break




