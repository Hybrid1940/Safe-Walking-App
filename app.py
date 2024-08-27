from flask import Flask, render_template, request, redirect, url_for, session
import speech_recognition as sr

app = Flask(__name__)

app.secret_key = 'ayushe'

@app.route("/")
def index(): 
    return render_template("index.html")
    
@app.route('/emergency_calls', methods=['GET', 'POST'])
def emergency_calls():
    return render_template('emergency_calls.html')

@app.route('/set_safe_word', methods=['POST'])
def set_safe_word():
    session['safe_word'] = request.form['safe_word']
    session['phone_number'] = request.form['phone_number']
    return redirect(url_for('index'))

def listen_for_safe_word():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("Listening for the safe word...")
        audio = recognizer.listen(source)
    
    try:
        transcript = recognizer.recognize_google(audio)
        if session.get('safe_word') and session['safe_word'].lower() in transcript.lower():
            # trigger_emergency_call()
            print("trigger word detected--emergency call initiated")
        else:
            print("Safe word not detected.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

# def trigger_emergency_call():
#     phone_number = session.get('phone_number')
#     if phone_number:
#         print(f"Emergency call triggered to {phone_number}!")
#         # Add actual call logic here--add twillio to call
#     else:
#         print("Phone number not found!")

@app.route('/start_listening')
def start_listening():
    listen_for_safe_word()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)