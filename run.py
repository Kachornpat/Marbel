from flask import Flask, render_template
import os

app = Flask(__name__)

project_list = [{"id": 1, "name": "Marbel"}, {"id": 2, "name": "Atlas"}]


task_list = [{"id": 1, "name": "Model"}, {"id": 2, "name": "Sculpt"}]


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html", title="Home", project_list=project_list, task_list=task_list
    )


@app.route("/project")
def project():
    return render_template("project_detail.html", title="Project", project_list=project_list)


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    return render_template("project_detail.html", title="Project", project_id=project_id)


@app.route("/task")
def task():
    return render_template("task_detail.html", title="Task", task_list=task_list)


@app.route("/task/<int:task_id>")
def task_detail(task_id):
    return render_template("task_detail.html", title="Task", task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)
