import speech as s
import datetime 

if __name__ == "__main__":
    while True:
        query = s.takeCommand().lower()
 
       
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print("The time is {}".format(strTime))
            s.speak("The time is {}".format(strTime))
 
    
        elif 'nick'or 'nicholas' or 'joseph' in query:
            nick1 = "Everybody calls me Fury. not nicholas, not joseph, not nick. just. fury."
            print(nick1)
            s.speak(nick1)
            
        elif 'what does your mom call you' or 'what do you call your mom' or 'what would your kids call you'  in query:
            nick2 = "fury"
            print(nick2)
            s.speak(nick2)

        elif  'leave' in query:
            print("Goodbye Sir. Have a nice day.")
            s.speak("Goodbye Sir. Have a nice day.")
            break
 

