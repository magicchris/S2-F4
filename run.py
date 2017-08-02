from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/B20769')
def details():
	return render_template('B20769.html')

if __name__ == '__main__':
    app.run(debug = True)