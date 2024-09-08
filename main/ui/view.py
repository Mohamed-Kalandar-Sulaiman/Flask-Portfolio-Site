from flask import Blueprint, render_template, request
from datetime import datetime 
import os

ui_blueprint = Blueprint(
    "ui",
    __name__,
    template_folder="templates", 
    static_folder="static", 
    static_url_path="/ui"
)

log_file_path = "visitor_logs.txt"

@ui_blueprint.route("/", methods=['GET'])
def home():
    queryParams = request.args
    origin = queryParams.get("origin", "unknown")
    
    if origin != "me":
        # Collect detailed information about the visitor
        client_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        referrer = request.referrer if request.referrer else "No referrer"
        full_url = request.url
        http_method = request.method
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Create a detailed log entry
        log_data = (
            f"[{timestamp}] IP: {client_ip}, "
            f"User-Agent: {user_agent}, "
            f"Referrer: {referrer}, "
            f"URL: {full_url}, "
            f"Method: {http_method}, "
            f"Origin: {origin}\n"
        )
        
        # Write log data to the log file
        with open(log_file_path, "a") as log_file:
            log_file.write(log_data)
        
        # Print log details to the console (optional)
        print(f"Profile viewed: {log_data}")
    
    return render_template("home.html")

@ui_blueprint.route("/logs", methods=['GET'])
def logs():
    # Check if the log file exists
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as log_file:
            log_content = log_file.read()
    else:
        log_content = "No logs available."
    
    return f"<pre>{log_content}</pre>"
