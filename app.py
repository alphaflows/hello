from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello1():
    return 'Test Successfully'

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)