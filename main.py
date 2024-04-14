import os
import time
import webbrowser
import playsound
import speech_recognition as sr
import datetime
import openaitest
import openai
import pyttsx3

#Future ideas: Weather API, NewsAPI

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()                                     #creating recognition object
    with sr.Microphone() as source:                         #can use a different source, like a text file
        r.adjust_for_ambient_noise(source,duration=1)       #reminder: delay of 1 sec due to adjusting recognizer's energy threshold 
        audio=r.listen(source)                              #use speech recognizer to listen to the microphone
        spoken = ""

        try:
            spoken=r.recognize_google(audio, language = "en-US")    #uses google api to recognise what user said
            print(spoken)

        except Exception as e:                                      #if no input
            print("All quiet here..." + str(e))
    
    return spoken



def ai(promp):
    
    #Enter your OpenAI API Key here:
    openai.api_key = 
    
    prompt = promp
    text = f"GPT Response for Prompt: {prompt}\n\n"
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "System Message"}, {"role": "user", "content": prompt}],
      temperature=0.5,
      max_tokens=300
    )

    #print(response.choices[0].message['content'])
    speak(response.choices[0].message['content'])

    text += response.choices[0].message['content']

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    
    with open(f"OpenAI/{''.join(prompt.split('GPT'.lower())[1:]).strip()}.txt", "w") as f:
    
        f.write(text)




speak("Hello, I am TARS, and this is my first demo")

while True:
    print("Listening...")
    text = get_audio()

    ########
  
    sites = [["Google", "https://google.com"], ["Youtube", "https://youtube.com"], ["LinkedIn", "https://linkedin.com"], 
           ["Instagram", "https://instagram.com"], ["Spotify", "https://spotify.com"], ["Flex", "https://flexstudent.nu.edu.pk/Login"]]

    for site in sites:
        if f"open {site[0]}".lower() in text.lower():
            t = f"Opening {site[0]}"
            speak(t)
            webbrowser.open(site[1])
        
    ########

    if "the time".lower() in text.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strfTime}")          
        
    ########
  
    if "gpt".lower() in text.lower():
        ai(text)

    ########

    if "close program".lower() in text.lower():
        speak("Closing Program")
        break


