from flask import Blueprint, render_template
from flask import request
ui_blueprint = Blueprint("ui", __name__, template_folder="templates", static_folder="static", static_url_path="/ui")

@ui_blueprint.route("/", methods=['GET'])
def home():

    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    print("IP ", client_ip)    
    return render_template("home.html")


