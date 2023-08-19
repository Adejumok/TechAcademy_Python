from flask import Flask, request, jsonify
from flask_cors import CORS
from entry import *

app = Flask(__name__)
CORS(app)


@app.route('/api/speech-recognition', methods=['GET'])
def speech_recognition():
    try:
        print("Request received at speech-recognition endpoint")
        speak("Hello! Enter the name to be queried")
        user_input = listen()

        if user_input:
            speak("You said: " + user_input)
        else:
            speak("Sorry, I didn't catch that.")

        speak("Name received!")

        speak("Enter the Subject")

        subject = listen()

        if subject:
            speak("You said: " + subject)
        else:
            speak("Sorry, I didn't catch that.")

        speak("Subject Received")

        speak("Enter your comment")

        comment = listen()

        if comment:
            speak("You said: " + comment)

        else:
            speak("Sorry, I didn't catch that.")

        speak("Comment Received")

        result = subject
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
