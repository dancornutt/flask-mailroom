import os
import base64

from flask import Flask, render_template, request, redirect, url_for

from model import Donor, Donation

from flask_nav import Nav
from flask_nav.elements import Navbar, View, Separator

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
        amount = float(request.form['amount'])
        donor = Donor(name=request.form['donor'].title())
        donor.save()
        Donation(value=amount, donor=donor).save()
        return redirect(url_for('all'))
    else:
        return render_template('donate.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
