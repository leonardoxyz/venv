from flask import Flask

app = Flask(__name__)

@app.put('/')
def hellow_world():
    return 'Hello caraio'

if (__name__ == '__main__'):
    app.run()