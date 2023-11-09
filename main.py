import speech as s
import datetime 

if __name__ == "__main__":
    while True:
        query = s.takeCommand().lower()
 
       
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print("Sir, the time is {}".format(strTime))
            s.speak("Sir, the time is {}".format(strTime))
 

         
        if  'leave' in query:
            print("Goodbye Sir. Have a nice day.")
            s.speak("Goodbye Sir. Have a nice day.")
            break
 

