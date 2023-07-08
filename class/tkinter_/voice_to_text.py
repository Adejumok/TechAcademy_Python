import tkinter as tk
import speech_recognition as sr
from moviepy.editor import AudioFileClip

# Create a Tkinter window
window = tk.Tk()


# Function to recognize speech and update the text label
def recognize_speech():
    recognizer = sr.Recognizer()

    rose_voice = 'C:\\Users\\rose.adeyinka\\PycharmProjects\\pythonProject\\class\\twinker\\lag_voice.mp3'

    audio_clip = AudioFileClip(rose_voice)
    temp_wav_file = "temp.wav"
    audio_clip.write_audiofile(temp_wav_file)

    with sr.AudioFile(temp_wav_file) as aud_file:
        audio_ = recognizer.record(aud_file)
        text = recognizer.recognize_google(audio_)
        text_label.configure(text="Recognized Text: " + text)

    # Clean up temporary WAV file
    import os
    os.remove(temp_wav_file)


# Create a label to display the recognized text
text_label = tk.Label(window, text="Recognized Text: ")
text_label.pack()

# Create a button to initiate speech recognition
button = tk.Button(window, text="Recognize Speech", command=recognize_speech)
button.pack()

# Run the Tkinter event loop
window.mainloop()
