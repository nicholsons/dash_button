from flask import Flask, redirect, render_template
from dash import Dash, html


flask_app = Flask(__name__)
dash_app = Dash(__name__, server=flask_app, url_base_pathname='/dashboard/')
dash_app.layout = html.Div([html.H1('I am a dashboard app')])


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/dashboard')
def render_dash():
    return redirect('/dashboard/')


if __name__ == '__main__':
    flask_app.run(debug=True)
