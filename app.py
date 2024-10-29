from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return "G'day visitor!"

if __name__ == '__main__':
    app.run(debug=True)