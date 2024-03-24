from flask import Flask, url_for, redirect, render_template, request
from ai import generate_image

app = Flask(__name__)
   
@app.route('/generate')
def generate():
    prompt = None
    # Add codes to handle GET request args
    # If args exists, pass the prompt into generate_image()
    return render_template('generate.html', prompt=prompt)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=False, port=5111)