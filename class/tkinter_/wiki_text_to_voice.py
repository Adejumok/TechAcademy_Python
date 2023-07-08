from gtts import gTTS
import wikipedia
import os

result = wikipedia.summary("Chicken", sentences=5)

# mytext= 'Lagos is a good city'
language = 'en'
myobj = gTTS(text=result, lang=language, slow=False)
myobj.save('chick_voice.mp3')
os.system('mediaplayer chick_voice.mp3')
