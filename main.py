import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation

from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Separator

app = Flask(__name__)
nav = Nav(app)

nav.register_element('my_navbar', Navbar(
    'thenav',
    View('Home Page', 'home'),
    View('Donate', 'donor')
))


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/donate/')
def donor():
    donations = Donation.select()
    return render_template('donate.jinja2', donations=donations)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
