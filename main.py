from flask import Flask, request, render_template
from flask_recaptcha import ReCaptcha
import os

# Initialize app instance
app = Flask(__name__)
app.config['RECAPTCHA_ENABLED'] = True
# Call recaptcha settings from environment variables
app.config['RECAPTCHA_SITE_KEY'] = os.getenv('RECAP_SITE')
app.config['RECAPTCHA_SECRET_KEY'] = os.getenv('RECAP_SECRET')

# Initialize recaptcha instance providing site key, secret key and app instance
recaptcha = ReCaptcha(app=app,
                      secret_key=app.config['RECAPTCHA_SECRET_KEY'],
                      site_key=app.config['RECAPTCHA_SITE_KEY'],
                      is_enabled=app.config['RECAPTCHA_ENABLED'])

# An over-simplified function to validate form input
def validate_text(input_field):
    if len(input_field) > 0 and len(input_field) <= 20:
        return True

# Route to submit and render form
@app.route('/submit', methods=['POST', 'GET'])
def submit():

    # If request is GET (form submit button is not pressed)
    if request.method == 'GET':
        return render_template('form.html')
    # If form submit button is pressed (POST method)
    elif request.method == 'POST':
        # If recaptcha verifies successfully
        if recaptcha.verify():
            username = request.form.get('username')
            password = request.form.get('password')
            # Validate form data, return Success if true
            if validate_text(username) and validate_text(password):
                return '<h1>Success.</h1>'
            # Return an error otherwise.
            error = 'There was a problem with input fields, ensure they\'re between 1-20 characters.'
            return render_template('form.html', error=error)
        else:
            # if Captcha fails, return an error.
            error = 'Captcha verification has failed, try again.'
            return render_template('form.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)