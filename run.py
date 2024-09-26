from flask import Flask, render_template
import os

app = Flask(__name__)

project_list = [
    {
        "id": 1,
        "name": "Marbel"
    },
    {
        "id": 2,
        "name": "Atlas"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home", project_list=project_list)


@app.route("/project/<int:project_id>")
def project(project_id):
    return render_template("project.html", title="Project", project_id=project_id)


if __name__ == "__main__":
    app.run(debug=True)
