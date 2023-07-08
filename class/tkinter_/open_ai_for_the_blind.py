import openai

openai.api_key = "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"


def convert_text_to_speech(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=500,
        temperature=0.8,
        voice='en-US-Wavenet-D'
    )

    audio_url = response.choices[0].audio

    # Perform further processing or playback of the audio URL
    # For example, you can save the audio to a file or stream it to a media player


# Example usage
text_to_convert = "Hello, how are you?"
convert_text_to_speech(text_to_convert)
