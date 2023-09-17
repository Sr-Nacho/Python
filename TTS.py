"""
By Miles Elkins
Below is kind of a long story, so skip it if you feel like it
With help from ChatGPT to do the if/elif/else statements
This made it so that inputs were male/female rather than voices[0].id/voices[1].id
ChatGPT did not contribute any important parts of the code, it simply increased user friendliness
Because of this, I went out to learn if/elif/else ststements, and now i can do things like this myself
"""

# Set up the library
import pyttsx3
engine = pyttsx3.init()

# Choose the voice based on user input(ChatGPT assisted)
gender_input = input("Enter 'male' or 'female' to pick a voice: ")

if gender_input == 'male':
    engine.setProperty('voice', voices[0].id)
elif gender_input == 'female':
    engine.setProperty('voice', voices[1].id)
else:
    print("Voice not found for the specified gender.")

#Choose to save as mp3 or say as words 
print("Save as mp3 or say immediately? ")
output_type = input("mp3/say: ")

#Save/Say
if output_type == "say":
    #Say the words
    words = input("What should I say? ")
    
    engine.say(words)
    engine.runAndWait()
elif output_type == "mp3":
    #Save as mp3
    words = input("What should I save? ")
    file_name = input("What should it be called? ")
    
    engine.save_to_file(words, file_name)
    engine.runAndWait()
else:
    print("That is not a valid response.")
    engine.say("That is not a valid response")
    engine.runAndWait()
