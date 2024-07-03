from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello1():
    return 'Hello World'

@app.route('/hello')
def hello():
    return 'Hello!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)