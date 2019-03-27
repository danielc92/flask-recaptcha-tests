from flask import Flask, request, render_template
from flask_recaptcha import ReCaptcha
import os


app = Flask(__name__)
app.config['RECAPTCHA_ENABLED'] = True
app.config['RECAPTCHA_SITE_KEY'] = os.getenv('RECAP_SITE')
app.config['RECAPTCHA_SECRET_KEY'] = os.getenv('RECAP_SECRET')


recaptcha = ReCaptcha(app=app,
                      secret_key=app.config['RECAPTCHA_SECRET_KEY'],
                      site_key=app.config['RECAPTCHA_SITE_KEY'],
                      is_enabled=app.config['RECAPTCHA_ENABLED'])


def validate_text(input_field):
    if len(input_field) > 0 and len(input_field) <= 20:
        return True


@app.route('/submit', methods=['POST', 'GET'])
def submit():

    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        if recaptcha.verify():
            username = request.form.get('username')
            password = request.form.get('password')
            if validate_text(username) and validate_text(password):
                return '<h1>Success.</h1>'

            error = 'There was a problem with input fields, ensure they\'re between 1-20 characters.'
            return render_template('form.html', error=error)
        else:
            error = 'Captcha verification has failed, try again.'
            return render_template('form.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)