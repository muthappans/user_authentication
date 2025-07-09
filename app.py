from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "f2c9fcb8b95f492bb4e0c52de37aa17ad1208f50c9c60b31d4fcabc44e4f6f38"
bcrypt = Bcrypt(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["flask_auth_db"]
users_collection = db["users"]

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        age = request.form.get("age")
        phone = request.form.get("phone")

        if users_collection.find_one({"email": email}):
            flash("That email is already registered.", "error")
            return redirect(url_for("register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password,
            "age": age,
            "phone": phone
        })

        flash("You're all set! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = users_collection.find_one({"email": email})

        if user and bcrypt.check_password_hash(user["password"], password):
            session["username"] = user["name"]
            return redirect(url_for("dashboard"))

        flash("Wrong email or password.", "error")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])

    flash("You need to log in first.", "warning")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    flash("You’ve been logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
