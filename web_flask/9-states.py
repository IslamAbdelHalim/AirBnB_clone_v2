#!/usr/bin/python3
"""
 list states
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays an HTML page"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Dislplay State"""
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    for state in states:
        if id == state.id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html", state=None)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
