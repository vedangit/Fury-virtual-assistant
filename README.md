# Fury - A virtual assistant
This Python project implements a simple voice assistant inspired by the character Nick Fury from the Marvel Universe. The assistant is capable of performing various tasks, such as providing the current time, answering questions about the assistant's name, searching Wikipedia for information, and interacting with web browsers.

## Prerequisites
Before running the program, make sure you have the required libraries installed. All the requirements are listed in the requirements.txt file. You can install them using the following command:

    `pip install -r requirements.txt`

## File Structure
main.py: The main script that acts as the entry point for the voice assistant.
speech.py: Module containing functions for speech synthesis and speech recognition.

## Usage
Run the main.py script to start the voice assistant.

    `python main.py`
    
The assistant will continuously listen for your voice commands

## Features
### 1. Time Information
Command: "time"
The assistant responds with the current time.

### 2. Name Inquiry
Commands: "nick", "nicholas", "joseph"
The assistant responds with a predefined answer indicating that it is called "Fury."

### 3. Personal Name
Commands: "What does your mom call you?", "What do you call your mom?", "What would your kids call you?"
The assistant responds with the name "Fury."

### 4. Wikipedia Search
Command: "wikipedia [topic]"
The assistant searches Wikipedia for the specified topic, providing the Wikipedia page link and the first three lines of the page.

### 5. Open YouTube
Command: "open youtube"
The assistant opens the YouTube website in the default web browser.

### 6. Search YouTube
Command: "search youtube"
The assistant asks for a search query and opens the YouTube search results in the default web browser.

### 7. Search Google
Command: "search google"
The assistant asks for a search query and opens the Google search results in the default web browser.

### 8. Leave
Command: "leave"
The assistant bids goodbye and exits the program.

### Web Browser Interaction
The webbrowser library is used to interact with web browsers for opening specific websites and performing searches.


## Additional Notes
The voice assistant uses the pyttsx3 library for text-to-speech synthesis and the SpeechRecognition library for speech recognition.
Wikipedia searches are performed using the Wikipedia library, and exceptions are handled for cases such as disambiguation pages or page not found.
Feel free to explore and enhance the functionality of this voice assistant!

