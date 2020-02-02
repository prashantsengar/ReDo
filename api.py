import random
import wiki
import yt
from flask import Flask, render_template, flash, request, send_file, Response, jsonify

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567dasghdj3'

qs = ['best out of waste ', 'how to reuse ', 'how to recycle ', 'make a from a ']

@app.route('/text/<item>')
def get_data(item):
    q = random.choice(qs)
    q = q + item
    text = wiki.get_results(q)
    return jsonify(text)

@app.route('/video/<item>')
def get_videos(item):
    q = random.choice(qs)
    q = q + item
    text = yt.get_data(q)
    return jsonify(text)


if __name__=='__main__':

    app.run('localhost',5000, debug=True)
