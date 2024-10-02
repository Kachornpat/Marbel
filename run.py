from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b71aa6324cb02548a704cf0a1c0db17'


project_list = [{"id": 1, "name": "Marbel"}, {"id": 2, "name": "Atlas"}]
task_list = [{"id": 1, "name": "Model"}, {"id": 2, "name": "Sculpt"}]

@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html", title="Home", project_list=project_list, task_list=task_list
    )

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Log in", form=form)


@app.route("/project/<int:project_id>")
def project_detail(project_id):

    project_name = ""

    for project in project_list:
        if project['id'] == project_id:
            project_name = project['name']
    return render_template(
        "project_detail.html",
        title="Project",
        project_name=project_name,
        task_list=task_list,
    )


@app.route("/task/<int:task_id>")
def task_detail(task_id):
    return render_template("task_detail.html", title="Task", task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)
