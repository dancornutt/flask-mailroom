import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session, flash

from model import Donation

from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Separator
from forms import DonorForm

app = Flask(__name__)
nav = Nav(app)

app.secret_key = b'\x92+\x9b\x0fK{\xc1m\xe5\xe0\xaee\xbe\xcfA\xb0\xe9j|\xce\x8c\xa2\xc0\xf4'


nav.register_element('my_navbar', Navbar(
    'thenav',
    View('Home Page', 'home'),
    View('Donate', 'donate'),
    Separator()
))


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/donate/', methods=['GET', 'POST'])
def donate():

    if request.method == "POST":
        donation = float(request.form['amount'])
        person = request.form['donor']
        session['donation'] = donation
        session['person'] = person
        print("it was {} who donated {}".format(person, donation))
    return render_template('donate.jinja2', session=session)


@app.route('/save/', methods=['POST'])
def save():
    print("I should save.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
