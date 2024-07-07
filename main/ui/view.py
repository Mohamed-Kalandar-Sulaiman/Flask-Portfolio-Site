from flask import Blueprint, render_template
from flask import request
ui_blueprint = Blueprint( "ui",
                          __name__,
                          template_folder="templates", 
                          static_folder="static", 
                          static_url_path="/ui"
                          )



@ui_blueprint.route("/", methods=['GET'])
def home():
    queryParams = request.args
    whoIsIt = queryParams.get("me",None)
    if whoIsIt== None :
        client_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        print("IP ", client_ip)    
        print("User Agent ", user_agent)    

    return render_template("home.html")


