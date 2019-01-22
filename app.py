from flask import Flask, render_template, jsonify
from vega_datasets import data

import altair as alt
import pandas as pd

alt.data_transformers.enable('default', max_rows=None)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vega-example')
def vega():

    df = pd.read_csv('2018_08_17_0013_2018-08-17--high-reti.csv.gz')

    chart = alt.Chart(df).mark_point().encode(
                x='flight_datetime:T',
                y='ALTITUDE_STANDARD:Q',
            )
    return jsonify(
            chart.to_dict()
           )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

