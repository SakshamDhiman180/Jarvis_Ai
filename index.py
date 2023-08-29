import speech_recognition as sr
from gtts import gTTS
import os
import openai

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
            openai.api_key = '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'
            prompt = "User: " + term  + "\nAssistant:"
            completion = openai.Completion.create(
                engine="text-davinci-003",  
                prompt=prompt,
                max_tokens=50 
                )
            response = completion.choices[0].text.strip()

            if response:
                response = f"I found this result for '{term}': {response}"
            else:
                response = f"I'm sorry, I couldn't find any results for '{term}'"
        elif "what is your name" in user_input.lower():
             response = f"Hi my name is JARViS ai asistant. Developed by Ssksham Dhiman"
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
