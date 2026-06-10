from flask import Flask, render_template_string

app = Flask(__name__)

coffee = {
    "Cold Brew": 0,
    "Latte": 0,
    "Cappuccino": 0
}

HTML = """
<h1>Coffee Rating App</h1>

{% for name,vote in coffee.items() %}
<form action="/vote/{{name}}" method="POST">

<h3>{{name}}</h3>

Votes: {{vote}}

<button type="submit">
Vote
</button>

</form>

<hr>

{% endfor %}
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        coffee=coffee
    )

@app.route("/vote/<name>", methods=["POST"])
def vote(name):
    coffee[name]+=1
    return home()

app.run(debug=True)