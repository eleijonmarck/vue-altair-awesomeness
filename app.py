from flask import Flask, render_template, jsonify
from vega_datasets import data

import altair as alt
import pandas as pd

alt.data_transformers.enable('default', max_rows=None)

app = Flask(__name__)

df = pd.read_csv('data/2018_08_17_0013_2018-08-17--high-reti.csv.gz')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vega-example')
def example():

    attributes = [
        'FUEL_FLOW_1:Q', 
        'FUEL_FLOW_2:Q', 
    ]

    base = alt.Chart().mark_line().encode(
        x='flight_datetime:T',
    )

    chart = alt.hconcat(data=df)

    for y_encoding in attributes:
        row = base.encode(
            y=y_encoding,
        )
        
        chart |= row
        
    return jsonify(
        chart.to_dict()
    )

@app.route('/vega-altitude')
def vega_altitude():

    attributes = [
        'ALTITUDE_STANDARD:Q', 
        'ALTITUDE_BARO:Q', 
    ]

    base = alt.Chart().mark_line().encode(
        x='flight_datetime:T',
    )

    chart = alt.hconcat(data=df)

    for y_encoding in attributes:
        row = base.encode(
            y=y_encoding,
        )
        
        chart |= row
        
    return jsonify(
        chart.to_dict()
    )

@app.route('/vega-latlong')
def latlong():

    points = alt.Chart(
        df
    ).mark_circle().encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        size=alt.value(10),
        color=alt.value('steelblue')
    )
       
    return jsonify(
        points.to_dict()
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)