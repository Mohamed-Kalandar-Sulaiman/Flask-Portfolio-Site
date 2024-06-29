from flask import Blueprint, render_template

ui_blueprint = Blueprint("ui", __name__, template_folder="templates", static_folder="static", static_url_path="/ui")

@ui_blueprint.route("/", methods=['GET'])
def home():
    return render_template("home.html")
