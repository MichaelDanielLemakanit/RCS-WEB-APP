from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/school-life')
def school_life():
    return render_template('school_life.html')

@app.route('/enrol')
def enrol():
    return render_template('enrol.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/login')
def login():
    return render_template('login.html')






if __name__ == '__main__':

    app.run(debug=True)