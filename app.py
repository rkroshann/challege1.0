from flask import Flask, session, abort, render_template

app = Flask(__name__)
app.secret_key = "Mczjsn6"

@app.route("/")
def index():
    session["role"] = "user"
    session["user"] = "guest"
    return render_template("index.html")

@app.route("/admin")
def admin():
    if session.get("role") == "admin" and session.get("user") == app.secret_key[::-1]:
        return render_template("admin.html")
    else:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

