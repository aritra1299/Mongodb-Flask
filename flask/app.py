from flask import Flask,render_template,request,redirect
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["local"]
collection = db["c1"]


app = Flask(__name__)

@app.route('/')
def home():
    return "Apurba"

@app.route('/form')
def form():
    return render_template("index.html")

@app.route('/submit',methods=['get','post'])
def submit():
    data=request.form.get("username")
    collection.insert_one({"username":data})
    return redirect("/display")

@app.route("/display")
def display():
    data=collection.find({})
    return render_template("display.html",datas=data)

if __name__ == '__main__':
    app.run(debug=True)
    
