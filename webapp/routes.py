from webapp import app
from flask import request, render_template

@app.route('/')
def _index():
    return render_template('index.html', headers=dict(request.headers))
