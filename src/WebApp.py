import os
from flask import Flask, redirect, url_for, render_template, request
from BM import BM
from Program import process

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        pattern = request.form["key"]
        return redirect(url_for("result", patt=pattern))
    else:
        return render_template("index.html")

@app.route("/result/<patt>", methods =["POST", "GET"])
def result(patt):
    if request.method == "POST":
        pattern = request.form["key"]
        return redirect(url_for("result", patt=pattern))
    else: # tergantung kepada input user
        database = os.listdir("../data")
        hasil = []
        for i in range (len(database)):
            hasil += process("../data/" + database[i], patt)
        if not(hasil):
            return render_template("index.html", list=[["Tidak ditemukan", ""]])
        else:
            return render_template("index.html", list=hasil)

if __name__ == "__main__":
    app.run()(debug=True)