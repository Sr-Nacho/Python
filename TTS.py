"""
By Miles Elkins
With help from ChatGPT to do the if/elif/else statements
This made it so that inputs were male/female rather than voices[0].id/voices[1].id
ChatGPT did not contribute any important parts of the code, it simply increased user friendliness
"""

# Set up the library
import pyttsx3
engine = pyttsx3.init()

# Choose the voice based on user input
gender_input = input("Enter 'male' or 'female' to pick a voice: ")

if gender_input == 'male':
    engine.setProperty('voice', voices[0].id)
elif gender_input == 'female':
    engine.setProperty('voice', voices[1].id)
else:
    print("Voice not found for the specified gender.")

# Say the words
words = input("What should I say? ")

engine.say(words)
engine.runAndWait()
