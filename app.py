"""
flask-deploy-demo - small Flask app used for a CI/CD demo.
Rohit Patil — kept intentionally simple so the focus is automation.
"""
import logging
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config

# configure basic logging so logs show up in Docker/Render/Actions logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    logging.info("Serving index page")
    return render_template("index.html")

@app.route("/about")
def about():
    logging.info("Serving about page")
    return render_template("about.html")

@app.route("/submit", methods=["POST"])
def submit():
    text = request.form.get("text", "").strip()
    if text:
        msg = f"You typed: {text}"
        flash(msg)
        logging.info("User submitted text: %s", text)
    else:
        flash("Please type something before submitting.")
        logging.info("User submitted empty text")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))