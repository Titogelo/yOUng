"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, request
from google.appengine.api import mail
import json

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


@app.route('/message', methods=['GET', 'POST'])
def sent_message():
    email_from = request.form['email']
    text = request.form['message']
    subject = request.form['subject']

    message = mail.EmailMessage(sender="simplelandingpage@themailprovider.com",
                                subject="FOO web contact")

    message.to = ['sendit2me@themailprovider.com', 'sendit2me2@themailprovider.com']
    message.body = "From: %s \nSubject: %s \nMessage: %s" % (email_from, subject, text)

    message.send()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}