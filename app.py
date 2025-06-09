from flask import Flask, render_template, request
from socket_scanner import scan_with_nmap

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        target = request.form.get("target")
        scan_result = scan_with_nmap(target)
        if "error" in scan_result:
            error = scan_result["error"]
        else:
            result = scan_result
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
