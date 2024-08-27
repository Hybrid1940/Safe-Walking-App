from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html")
    
@app.route('/emergency_calls')
def emergency_calls():
    return render_template('emergency_calls.html')

if __name__ == '__main__':
    app.run(debug=True)