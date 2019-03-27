# Flask Recaptcha Tests
Testing functionality of Google's ReCaptchav2 with flask micro web framework application, using flask-recaptcha module. Includes a working example.

# Before you get started
Basic knowledge of flask and python. Understanding of html forms, posts, get requests.

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/flask-recaptcha-tests.git
```
**Modules/dependencies:**
- `flask`
- `flask-recaptcha`

Install the following dependences:
```sh
pip install flask flask-recaptcha
```

Running: 
```sh
python3 main.py
```

Routes: 
Use the following route to test the application
```sh
http://localhost:5000/submit
```

# Tests
- Tested submitting form without completing recaptchav2.
- Tested submitting form with completing recaptchav2.

# Contributors
- Daniel Corcoran

# Sources
- [flask-recaptcha github page](https://github.com/mardix/flask-recaptcha)