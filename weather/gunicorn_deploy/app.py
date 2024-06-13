import datetime
import back
from flask import Flask, request, render_template, redirect , Response
import requests

import json

app = Flask(__name__)

#API_Key="d5bb8e5e422846f1bba142931230511"
API_Key = "FWGQHHB3JCJ8L4MM8EUNRDPYQ"


@app.get("/error")
def error():
    return render_template('error.html')


@app.post("/result")
def search():
    """
    get post method with result url.
    """
    try:
        result = back.get_week_forecast(request.form['city'])
        print(result)
        return render_template('table.html',filtered_data=result),200
    except:
        error = 'Invalid credentials'
        return redirect('/error')
        # return render_template('index.html')


@app.route("/")
def index():
    return render_template('index.html'), 200




if __name__ == "__main__":
    app.run(host="0.0.0.0")

