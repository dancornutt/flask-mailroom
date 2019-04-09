import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session, flash

from model import Donation

from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Separator
from forms import DonorForm

app = Flask(__name__)
nav = Nav(app)

app.secret_key = '8dabc8efdccf880165a5db5e97cbfcd0'

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
    # form = DonorForm()
    #
    # if request.method == "POST":
    #     if form.validate() is False:
    #         flash('Error in input!')
    #         return render_template('donate.jinja2', form=form)
    #     else:
    #         all()
    # elif request.method == "GET":
    #     return render_template('donate.jinja2', form=form)
    return render_template('donate.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
