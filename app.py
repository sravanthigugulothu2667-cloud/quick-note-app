from flask import Flask, request, render_template_string

app = Flask(__name__)

notes=[]

HTML="""
<form method="POST">
<input name="note" placeholder="Write note">
<button>Save Note</button>
</form>

<h3>Saved Notes</h3>

{% for n in notes %}
<p>{{n}}</p>
{% endfor %}
"""

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        note=request.form["note"]
        notes.append(note)

    return render_template_string(HTML, notes=notes)

app.run(debug=True)