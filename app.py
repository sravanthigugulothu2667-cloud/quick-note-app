from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<form method="POST">
<input name="name" placeholder="Enter Name"><br><br>

<input name="bio" placeholder="Enter Bio"><br><br>

<input name="image" placeholder="Enter Image URL"><br><br>

<button type="submit">Generate</button>
</form>

{% if name %}
<hr>
<h2>{{name}}</h2>
<p>{{bio}}</p>
<img src="{{image}}" width="200">
{% endif %}
"""

@app.route("/", methods=["GET","POST"])

def home():
    name=""
    bio=""
    image=""

    if request.method=="POST":
        name=request.form["name"]
        bio=request.form["bio"]
        image=request.form["image"]

    return render_template_string(
        HTML,
        name=name,
        bio=bio,
        image=image
    )

app.run(debug=True)