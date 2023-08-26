import speech_recognition as sr
from googlesearch import search
from gtts import gTTS
import os


recognizer = sr.Recognizer()

while True:
    print("Listening...")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)
        
        if user_input.lower() == "exit":
            break
        
        response = None
        if "search" in user_input.lower():
            term = user_input.lower().replace("search", "")
            search_results = list(search(term, num_results=1, lang="en",timeout=5))
            if search_results:
                response = f"I found this result for '{term}': {search_results[0]}"
            else:
                response = f"I'm sorry, I couldn't find any results for '{term}'"
        elif "what is your name" in user_input.lower():
             response = f"Hi my name is JARViS ai asistant. Developed by SAksham Dhiman"
        else:
            response = "I'm sorry, I'm not sure what you're asking Saksham."
        
        print("J.A.R.V.I.S.:", response)
        
        jarvis_tts = gTTS(text=response, lang="en")
        jarvis_tts.save("jarvis_response.mp3")
        os.system("start jarvis_response.mp3")
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
