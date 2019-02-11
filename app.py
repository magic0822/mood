from flask import Flask, render_template, request, flash, session
import time, operator
from datetime import datetime
from operator import itemgetter
from itertools import groupby

app = Flask(__name__)

moods = [
    {
        'date': '01-01-2019',
        'mood': 'Good'
    },
    {
        'date': '01-02-2019',
        'mood': 'Bad'
    },
    {
        'date': '01-03-2019',
        'mood': 'So so'
    },
    {
        'date': '01-04-2019',
        'mood': 'nice'
    },
    {
        'date': '01-08-2019',
        'mood': 'Bad'
    },
    {
        'date': '01-09-2019',
        'mood': 'Bad'
    },
]

another_user_moods = [
    {
        'date': '01-01-2019',
        'mood': 'Good'
    },
    {
        'date': '01-04-2019',
        'mood': 'Bad'
    },
    {
        'date': '01-05-2019',
        'mood': 'So so'
    },
    {
        'date': '01-06-2019',
        'mood': 'nice'
    },
    {
        'date': '01-10-2019',
        'mood': 'Bad'
    },
]

username = 'admin'
password = 'secret'
streak_len = len(moods)


# check user login before showing the mood list
@app.route('/mood', methods=['GET'])
def mood_list():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html', streak_len=streak_len, moods=moods,
                               percentage=check_con(format_date(moods)))


# store the user's new adding moods with add time and input value
@app.route('/mood', methods=['POST'])
def add_mood():
    if request.method == 'POST':
        mood_val = request.form['mood'].strip().lower()
        if mood_val:
            moods.append({'date': time.strftime("%m-%d-%Y", time.localtime()), 'mood': mood_val})
        return render_template('index.html', streak_len=streak_len, moods=moods, percentage=check_con(format_date(moods)))


# verify user identification by username and password
@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == password and request.form['username'] == username:
        session['logged_in'] = True
    else:
        flash('Invalid!')
    return mood_list()


# convert the date in moods from date format to string
def format_date(mood):
    date_list = []
    for d in mood:
        date_list.append(d['date'])
        dates = [datetime.strptime(d, "%m-%d-%Y") for d in date_list]
        date_ints = sorted(set([d.toordinal() for d in dates]))
    return date_ints


# compare the formatted date of moods if they are consecutive
def check_con(date_list):
    for k, g in groupby(enumerate(date_list), lambda x: x[1]-x[0]):
        lst = list(map(itemgetter(1), g))
        percentage = len(lst) / streak_len
        if operator.__ge__(percentage, 0.5):
            return "{0:.0%}".format(percentage)
        else:
            return ':)'


if __name__ == '__main__':
    app.secret_key = '12345'
    app.run(debug=True)
