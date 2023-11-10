import speech as s
import datetime
import wikipedia 
import webbrowser
import os 

if __name__ == "__main__":
    while True:
        query = s.takeCommand().lower()
 

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print("The time is {}".format(strTime))
            s.speak("The time is {}".format(strTime))
 
        elif 'nick' in query or 'nicholas' in query or 'joseph' in query:
            nick1 = "Everybody calls me Fury. not nicholas, not joseph, not nick. just. fury."
            print(nick1)
            s.speak(nick1)

        elif 'what does your mom call you' in query or 'what do you call your mom' in query or 'what would your kids call you'  in query:
            nick2 = "fury"
            print(nick2)
            s.speak(nick2)
            
        elif 'wikipedia' in query:
            s.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                page = wikipedia.page(query)
                page_url = page.url
                page_content = wikipedia.summary(query, sentences=3)
                s.speak(f"Here is the Wikipedia link for {query}")
                print(f"Here is the Wikipedia link for {query}: {page_url}")
                s.speak(page_url)
                s.speak("Here are the first three lines of the Wikipedia page:")
                print("Here are the first three lines of the Wikipedia page:")
                s.speak(page_content)
                print(page_content)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation pages
                print("Wikipedia search resulted in a disambiguation page. Please provide a more specific query.")
                s.speak("Wikipedia search resulted in a disambiguation page. Please provide a more specific query.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found
                print("Sorry, I couldn't find information on that topic.")
                s.speak("Sorry, I couldn't find information on that topic.")


            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
 
        elif 'search youtube' in query:
            s.speak("What should I search for, Sir?")
            req = s.takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query={}".format(req))
 
        elif 'search google' in query:
            s.speak("What should I search for, Sir?")
            search = s.takeCommand()
            webbrowser.open("https://www.google.com/search?q={}".format(search))

        elif  'leave' in query:
            print("Goodbye. Have a nice day.")
            s.speak("Goodbye. Have a nice day.")
            break


