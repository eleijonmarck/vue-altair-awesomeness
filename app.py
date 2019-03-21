from flask import Flask, render_template, jsonify
from vega_datasets import data

import altair as alt
import pandas as pd

alt.data_transformers.enable("default", max_rows=None)
cars = data.cars()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vega-example1")
def vega_example1():

    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(x="Horsepower", y="Miles_per_Gallon", color="Origin", shape="Origin")
    )

    return jsonify(chart.to_dict())


@app.route("/vega-example2")
def vega_example2():

    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(y="Horsepower:Q", color="Origin:N")
        .interactive()
    )

    chart = chart.encode(x="Acceleration:Q") | chart.encode(x="Displacement:Q")

    return jsonify(chart.to_dict())


@app.route("/vega-example3")
def vega_example3():

    brush = alt.selection_interval()

    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            color=alt.condition(brush, "Origin:N", alt.value("gray")),
        )
        .add_selection(brush)
        .properties(width=250, height=250)
        .repeat(
            row=["Horsepower", "Miles_per_Gallon"],
            column=["Acceleration", "Displacement"],
        )
    )

    return jsonify(chart.to_dict())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
