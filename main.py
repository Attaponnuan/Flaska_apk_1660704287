from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, BU 1660704287'

if __name__ == '__main__':
    app.run(debug=True)