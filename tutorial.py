from flask import Flask, redirect, url_for, render_template, request
from apiCall import currencies, getExchangeRate
app = Flask(__name__)

#need path for the variable to know where to load it
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        valueBase = request.form["base"]
        input1 = valueBase[2] + valueBase[3] + valueBase[4]
        print(input1)

        valueTarget = request.form["target"]
        input2 = valueTarget[2] + valueTarget[3] + valueTarget[4]
        print(input2)

        answear = getExchangeRate(input1, input2)
        print(answear)
        return redirect(url_for('result', ans = answear))
    else:
        return render_template("index.html", currencies = currencies)


@app.route("/<ans>")
def result(ans):
    return render_template("result.html", ans = ans)

if __name__ == "__main__":
    app.run(debug = True)