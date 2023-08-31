import speech_recognition as sr
from gtts import gTTS
import os
import openai

while True:
    print("ACTIVE")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        
    try:    
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)
        if user_input.lower() == "friday":
            print("Listening...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio)
                print("You:", user_input)
                
                if user_input.lower() == "exit":
                    exit()
                
                response = None
                term = user_input.lower()
                openai.api_key = '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'
                prompt = "User: " + term  + "\nAssistant:"
                completion = openai.Completion.create(
                    engine="text-davinci-003",  
                    prompt=prompt,
                    max_tokens=50 
                    )
                response = completion.choices[0].text.strip()

                if response:
                    response = f"{response}"
                else:
                    response = f"I'm sorry, I couldn't find any results for '{term}'"
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
        elif "friday tell me something about yourself" in user_input.lower() or "tell me about yourself" in user_input.lower():
            response = f"Hi my name is Friday an ai asistant. Developed by Saksham Dhiman"
        elif user_input.lower() == "exit":
            exit()      
        else:
            response = "I'm sorry, I'm not sure what you're asking Sir."
                
        print("F.R.I.D.A.Y.:", response)
        
        jarvis_tts = gTTS(text=response, lang="en")
        jarvis_tts.save("friday_response.mp3")
        os.system("start friday_response.mp3")
        
    except sr.UnknownValueError:
        print("Could not understand audio")
