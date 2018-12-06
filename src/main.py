#
#   This file is a part of "Questionario Pari Opportunità Treviglio";
# 	Copyright (c) 2018 The project Authors and Contributors (see AUTHORS and CONTRIBUTORS).
# 	See LICENSE file for further details:
# 	https://github.com/MarcoBuster/QuestionarioPariOpportunitaTreviglio/blob/master/LICENSE
#

import sqlite3

from flask import Flask, request, render_template, send_from_directory, jsonify
from google.auth.transport import requests
from google.oauth2 import id_token

from . import config

app = Flask(__name__, template_folder='templates', static_url_path='')

conn = sqlite3.connect(config.DATABASE_FILE)
c = conn.cursor()
c.executescript(config.DATABASE_TABLE)
conn.commit()
conn.close()
del conn, c


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/grazie', methods=['GET'])
def thanks():
    return render_template('thanks.html')


@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')


@app.route('/questionario', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('questionario.html')

    req = request.form

    try:
        id_info = id_token.verify_oauth2_token(req.get('google_token'), requests.Request(), config.GOOGLE_CLIENT_ID)
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return "L'account inviato non corrisponde ad un account Google.", 403

        with sqlite3.connect(config.DATABASE_FILE) as conn:
            c = conn.cursor()
            c.execute("SELECT EXISTS(SELECT 1 FROM users WHERE id=?)", (id_info["sub"], ))
            r = c.fetchone()[0]
            if r == 1:
                return "Hai già risposto al questionario.", 429

            c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (id_info["sub"], id_info["given_name"],
                                                                id_info["family_name"], id_info["email"]))
            conn.commit()

    except ValueError:
        return "L'account inviato non esiste o non è riconosciuto.", 400

    first = second = third = None
    for element in req:
        if element.startswith("q6"):
            if req.get(element) == '1':
                first = element.lstrip("q6_")
            elif req.get(element) == '2':
                second = element.lstrip("q6_")
            elif req.get(element) == '3':
                third = element.lstrip("q6_")

    data = tuple()
    for element in config.FIELDS:
        if element == 'q6_orientamento-sessuale':
            data = (*data, first, second, third)
        if element.startswith('q6'):
            continue
        data = (*data, req.get(element, None))

    with sqlite3.connect(config.DATABASE_FILE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO answers VALUES ("
                  "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                  "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        conn.commit()

    return jsonify({'ok': True})


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('../static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../static/css', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('../static/images', path)
