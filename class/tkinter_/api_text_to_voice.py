import openai
from gtts import gTTS
import os


openai.api_key = "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"

prompt = "Software engineering"

model = "text-davinci-003"

response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
language = 'en'
voice_obj = gTTS(text=generated_text, lang=language, slow=False)

voice_obj.save('software_eng.mp3')
os.system('mediaplayer software_eng.mp3')