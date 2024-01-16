from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html");

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        input_text = request.form['input_text']
        return render_template('result.html', input_text=input_text)
    return render_template('index.html')

if __name__ == "__main__":
    app.run();
