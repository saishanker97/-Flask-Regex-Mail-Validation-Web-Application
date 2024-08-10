from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    action = request.form['action']
    if action == 'regex':
        test_string = request.form['test_string']
        regex = request.form['regex']
        matches = re.findall(regex, test_string)
        return render_template('results.html', matches=matches)
    elif action == 'validate_email':
        email = request.form['email']
        # Simple regex for email validation
        is_valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None
        return render_template('results.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
